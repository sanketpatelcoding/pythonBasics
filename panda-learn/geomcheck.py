import pandas as pd
import numpy as np
import re


def parse_lat_lon(value):
    """
    Convert latitude or longitude from various formats to decimal degrees.
    Handles DMS (e.g., 77°13'45.6"N), decimal minutes (e.g., 77°13.76'N),
    and decimal degrees (e.g., 77.2345).
    Returns float in decimal degrees (e.g., 77.2345 or -77.2345).
    """
    if pd.isna(value):  # Handle missing values
        return np.nan

    # Convert to string and strip whitespace
    value = str(value).strip()

    # Handle decimal degrees (e.g., 77.2345 or -77.2345)
    try:
        return float(value)
    except ValueError:
        pass

    # Regular expression to parse DMS or decimal minutes
    # Matches: 77°13'45.6"N, 77:13:45.6 N, 77 13.76 N, etc.
    pattern = r'(\d{1,3})[°\s:]+(\d{1,2}(?:\.\d+)?)?(?:[''\s:]+(\d{1,2}(?:\.\d+)?)?)?\s*([NSEW]?)'
    match = re.match(pattern, value, re.IGNORECASE)

    if not match:
        return np.nan  # Return NaN for unparseable formats

    degrees, minutes, seconds, direction = match.groups()
    degrees = float(degrees)
    minutes = float(minutes) if minutes else 0.0
    seconds = float(seconds) if seconds else 0.0
    direction = direction.upper() if direction else ''

    # Convert to decimal degrees
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

    # Apply direction (negative for S or W)
    if direction in ['S', 'W']:
        decimal = -decimal

    return round(decimal, 5)  # Round to 5 decimal places for precision


# Example usage with a sample DataFrame
data = {
    'lat': ["40°42'51.4\"N", "40 42.86 N", "40.715", "-40.715", None],
    'lon': ["74°00'21.6\"W", "74 00.36 W", "-74.006", "74.006", "74:00:21.6 E"]
}
df = pd.DataFrame(data)

# Apply conversion to lat and lon columns
df['lat_decimal'] = df['lat'].apply(parse_lat_lon)
df['lon_decimal'] = df['lon'].apply(parse_lat_lon)

print(df)

# Optional: Prepare for geometry creation (e.g., with GeoPandas)
try:
    import geopandas as gpd

    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df['lon_decimal'], df['lat_decimal'])
    )
    print("\nGeoDataFrame with geometry:")
    print(gdf)
except ImportError:
    print("\nGeoPandas not installed. Install with `pip install geopandas` to create geometries.")