BASE_WEIGHT = 0.10
VOL_ANCHOR = 0.00623  # fixed 2021 median of daily market_volatility
SCALE_MIN = 0.50
SCALE_MAX = 2.00


def generate_positions(history, current_date):
    latest = history.loc[history.date == current_date]
    market_vol = float(latest["market_volatility"].iloc[0])
    scale = min(SCALE_MAX, max(SCALE_MIN, VOL_ANCHOR / max(market_vol, 1e-12)))
    weight = BASE_WEIGHT * scale
    positions = {}
    for _, group in latest.groupby("sector", sort=False):
        ordered = group.sort_values(["carry_score", "asset_id"])
        short_id = ordered["asset_id"].iloc[0]
        long_id = ordered["asset_id"].iloc[-1]
        if short_id == long_id:
            continue
        positions[short_id] = -weight
        positions[long_id] = weight
    return positions
