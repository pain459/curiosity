
# SRE Metrics: Definitions and Examples

## 1. TTD (Time to Detect)
- **Definition**: The time it takes to detect an issue after it occurs.
- **Purpose**: Measures the effectiveness of monitoring and alerting systems.
- **Example**: If a service outage occurs at 10:00 AM and monitoring detects it at 10:02 AM, the TTD is **2 minutes**.

---

## 2. TTK (Time to Know)
- **Definition**: The time it takes for the incident team to understand and confirm the issue after detection.
- **Purpose**: Captures the time spent diagnosing or confirming the problem after detection.
- **Example**: If the issue is detected at 10:02 AM and confirmed by the team at 10:10 AM, the TTK is **8 minutes**.

---

## 3. TTM (Time to Mitigate)
- **Definition**: The time it takes to implement a temporary or partial fix to stop the issue's impact.
- **Purpose**: Evaluates the speed of containing the issue to reduce harm while working on a full resolution.
- **Example**: If the team confirms the issue at 10:10 AM and applies a mitigation at 10:20 AM, the TTM is **10 minutes**.

---

## 4. MTTR (Mean Time to Resolve)
- **Definition**: The average time it takes to fully resolve an issue after detection.
- **Purpose**: Measures the efficiency of the incident response and recovery process.
- **Formula**:  
  \[
  MTTR = rac{	ext{Total Time to Resolve Issues}}{	ext{Number of Issues}}
  \]
- **Example**: If two incidents took 30 and 60 minutes to resolve, the MTTR is:
  \[
  MTTR = rac{30 + 60}{2} = 45 \, 	ext{minutes}
  \]

---

## 5. Availability
- **Definition**: The percentage of time the system is operational and accessible to users.
- **Formula**:  
  \[
  	ext{Availability} = rac{	ext{Uptime}}{	ext{Uptime} + 	ext{Downtime}} 	imes 100
  \]
- **Example**: If the system is available for 43,190 out of 43,200 minutes in a month, availability is:
  \[
  rac{43,190}{43,200} 	imes 100 = 99.98\%
  \]

---

## 6. Latency Percentiles (P90, P95, P99)
- **P90 (90th Percentile)**: The value below which 90% of requests are completed.
- **P95 (95th Percentile)**: The value below which 95% of requests are completed.
- **P99 (99th Percentile)**: The value below which 99% of requests are completed.
- **Purpose**: Helps measure and optimize for tail-end performance (worst-case scenarios).
- **Example Dataset**: Response times: `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
  - **P90**: Rank = \( 0.9 	imes 10 = 9 \), value = **90 ms**.
  - **P95**: Rank = \( 0.95 	imes 10 = 9.5 \), interpolate to get **95 ms**.
  - **P99**: Rank = \( 0.99 	imes 10 = 9.9 \), interpolate to get **99 ms**.

---

## 7. Error Rate
- **Definition**: The percentage of failed requests out of total requests.
- **Formula**:  
  \[
  	ext{Error Rate} = rac{	ext{Number of Errors}}{	ext{Total Requests}} 	imes 100
  \]
- **Example**: If there are 100 failed requests out of 10,000, the error rate is:
  \[
  	ext{Error Rate} = rac{100}{10,000} 	imes 100 = 1\%
  \]

---

## 8. Burn Rate
- **Definition**: The speed at which your error budget is consumed.
- **Formula**:  
  \[
  	ext{Burn Rate} = rac{	ext{Actual Error Rate}}{	ext{Allowed Error Rate}}
  \]
- **Example**: If you're consuming your error budget at twice the allowed rate, the burn rate is **2x**.

---

## 9. MTBF (Mean Time Between Failures)
- **Definition**: The average time between two consecutive failures in a system.
- **Formula**:  
  \[
  MTBF = rac{	ext{Total Uptime Between Failures}}{	ext{Number of Failures}}
  \]
- **Example**: If a system runs without issues for 100 days before failing, the MTBF is **100 days**.

---

## 10. MTTA (Mean Time to Acknowledge)
- **Definition**: The average time it takes for a team to acknowledge an alert after it's triggered.
- **Purpose**: Measures responsiveness to incidents.
- **Example**: If it takes an average of 10 minutes to acknowledge alerts, the MTTA is **10 minutes**.

---

## 11. MTTC (Mean Time to Contain)
- **Definition**: The average time it takes to contain an issue and prevent further damage.
- **Purpose**: Helps measure incident containment efficiency, especially for cascading failures.
- **Example**: If it takes 2 hours to contain a data breach, the MTTC is **2 hours**.

---

## 12. Cost of Downtime
- **Definition**: The financial impact of system downtime.
- **Formula**:  
  \[
  	ext{Cost of Downtime} = 	ext{Duration of Downtime} 	imes 	ext{Revenue Lost Per Minute}
  \]
- **Example**: If the system generates $1,000/minute and is down for 10 minutes:
  \[
  	ext{Cost of Downtime} = 10 	imes 1,000 = 10,000 \, 	ext{USD}
  \]

---

## 13. Change Failure Rate
- **Definition**: The percentage of changes (e.g., deployments, patches) that result in failures.
- **Formula**:  
  \[
  	ext{Change Failure Rate} = rac{	ext{Number of Failed Changes}}{	ext{Total Changes}} 	imes 100
  \]
- **Example**: If 2 out of 10 deployments cause issues, the change failure rate is **20%**.

---

## 14. Incident Recurrence Rate
- **Definition**: The frequency of repeat incidents due to unresolved root causes.
- **Example**: If the same database issue occurs twice in a month, the recurrence rate is **2/month**.

---

## 15. First-Time Fix Rate
- **Definition**: The percentage of incidents resolved on the first attempt.
- **Example**: If 8 out of 10 incidents are resolved without follow-ups, the first-time fix rate is **80%**.
