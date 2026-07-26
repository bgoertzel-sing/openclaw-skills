from run_carom_gpt2_controller_v6 import select_scale_v6


def test_peak_guard_repairs_v5_update600_choice():
    predicted = {0.25: 1.8666, 0.5: 1.8349, 1.0: 1.8165, 1.5: 1.8143}
    assert select_scale_v6(predicted, 0.001836)[0] == 0.25


def test_forecast_remains_active_away_from_peak():
    predicted = {0.25: 1.6011, 0.5: 1.5981, 1.0: 1.6009, 1.5: 1.6028}
    assert select_scale_v6(predicted, 0.000197) == (0.5, "forecast_argmin")
