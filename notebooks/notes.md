## Engineered columns

### Lags (see historical consumption pattern, go back N days and grab that single value.)

lag_1 = quantity used 1 day prior
lag_7 quantity used 7 days prior

## Rolling mean
day:     1   2   3   4   5   6   7   8
usage:  10  14   9  12  20  11   8  13

A rolling mean with window 3 at each day is the average of that day and the 2 days before it:

day 3: (10+14+9)/3   = 11.0
day 4: (14+9+12)/3   = 11.7
day 5: (9+12+20)/3   = 13.7
day 6: (12+20+11)/3  = 14.3
day 7: (20+11+8)/3   = 13.0
day 8: (11+8+13)/3   = 10.7

Why it's useful: Raw daily usage jumps around (10, 14, 9, 12, 20...), which is noisy and hard to act on directly. The rolling mean smooths that out into a more stable trend line — day 5's rolling mean of 13.7 tells you "usage has been running around 13-14 lately," even though day 5 itself spiked to 20.

## Why bother with both?
lag_1 gives the model the exact most recent value — useful for catching "yesterday spiked, so today probably will too" (short-term momentum/autocorrelation).
rolling_mean_7 gives the model the smoothed recent level — useful for "what's the stable baseline right now, ignoring noise."

A model can use the gap between the two to detect something interesting: if lag_1 is way above rolling_mean_7, that's a signal "yesterday was unusually high relative to the recent trend"