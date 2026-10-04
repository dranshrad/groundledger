# Unit economics (Paid Cast `math`)

## Inputs (user-supplied)

| Input | Notes |
|-------|-------|
| Price / AOV | Or blended AOV |
| Gross margin % | After COGS; exclude vanity “markup” |
| Target CAC or payback days | Pick one primary |
| Conversion rate (site or trial) | Label source |
| LTV proxy | Optional; mark assumption strength |

## Outputs

- Break-even CPA / CAC  
- Contribution per conversion  
- Max viable CPC/CPM under assumed CVR  
- Scenario table: pessimistic / base / optimistic — each assumption listed  

## Rules

1. No silent industry benchmarks.  
2. If CVR is unknown, solve for the required CVR at a bid. Do not invent CVR.  
3. Blended account ROAS ≠ product truth. Segment when possible.  
4. Pass results into `budget` and `trial` modes as fences, not slogans.  
