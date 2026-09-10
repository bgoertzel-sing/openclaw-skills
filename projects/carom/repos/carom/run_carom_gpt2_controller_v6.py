"""V6 selection policy: retain v5 forecast away from the LR peak, guard peak."""


def select_scale_v6(predicted_losses, parent_lr, schedule_peak_lr=2e-3,
                    guard_fraction=0.75, guarded_scale=0.25):
    """Use the conservative scale in the empirically uncalibrated peak region."""
    if parent_lr >= guard_fraction * schedule_peak_lr:
        return guarded_scale, "peak_lr_guard"
    return min(predicted_losses, key=predicted_losses.get), "forecast_argmin"
