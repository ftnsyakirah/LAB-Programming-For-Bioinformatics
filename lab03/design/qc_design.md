## Problem

### Input
For classify_read:
- length (int) : read length
- n_count (int) : number of N bases
-gc (float) : GC percentage

For trim_low_quality:
- quals (list[int]): quality scores
- threshold (int): minimum acceptable quality

### Output
classify_read returns:
- "reject"
- "review"
- "pass"

trim_low_quality returns:
- index where the low-quality tail starts
- number of bases to keep

### Constraints
- If length < 500 → reject
- If n_count > 10 → review
- If GC < 30 or GC > 70 → review
- GC 30 and GC 70 are valid
- N count 10 is valid
- Length 500 is valid
- Quality scores equal to threshold are kept

## Pseudocode

### classify_read
SET MIN_LEN = 500
SET MAX_N = 10
SET GC_LOW = 30
SET GC_HIGH = 70

IF length < MIN_LEN
    RETURN "reject"

IF n_count > MAX_N OR gc < GC_LOW OR gc > GC_HIGH
    RETURN "review"

RETURN "pass"

### trim_low_quality
SET end = length of quals

WHILE end > 0 AND quals[end - 1] < threshold
    end = end - 1

RETURN end

## Flowchart

```text
                  Start
                    |
                length < 500?
              (yes)/     \(no)
               reject   n_count>10 OR gc<30 OR gc>70?
                  |                |
                review            pass

```

## Trace

| sample | length | n_count | gc | length < 500? | N > 10 or GC outside 30-70? | decision |
|---|---:|---:|---:|---|---|---|
| R03 | 420 | 0 | 68.5 | Yes | No | reject |
| R04 | 500 | 10 | 45.0 | No | No | pass |
| R05 | 640 | 3 | 72.4 | No | Yes | review |
| R07 | 499 | 0 | 50.0 | Yes | No | reject |