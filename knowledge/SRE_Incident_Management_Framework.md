
# SRE Incident Management Framework

## 1. Incident Overview
- **Incident ID**: `#<incident-id>`
- **Date/Time**: `<date-time>`
- **Service/System Affected**: `<service-or-system-name>`
- **Severity**: `<Critical/High/Medium/Low>`
- **Description**: `<brief-summary-of-incident>`
- **Customer Impact**:
  - **Affected Users**: `<number-or-percentage>`
  - **Lost Revenue**: `<estimated-revenue-loss>`
  - **Support Tickets**: `<number-of-related-tickets>`

---

## 2. Incident Timeline
| **Metric**                  | **Definition**                                  | **Example**                |
|-----------------------------|------------------------------------------------|----------------------------|
| **TTD (Time to Detect)**     | Time from occurrence to detection               | `<value>`                  |
| **TTK (Time to Know)**        | Time from detection to confirmation/diagnosis  | `<value>`                  |
| **TTM (Time to Mitigate)**    | Time from diagnosis to mitigation              | `<value>`                  |
| **MTTI (Time to Identify)**   | Time to identify the root cause                | `<value>`                  |
| **MTTR (Time to Resolve)**    | Time to fully resolve the issue                | `<value>`                  |

---

## 3. RCA (Root Cause Analysis)
- **Problem Statement**: `<what-happened>`
- **Root Cause**: `<underlying-cause>`
- **Supporting Evidence**: `<logs/metrics/screenshots>`
- **Contributing Factors**: `<secondary-issues>`

---

## 4. Metrics Tracking
| **Metric**               | **Purpose**                                      | **Example**                |
|--------------------------|--------------------------------------------------|----------------------------|
| **Availability**          | Percentage of uptime                            | `<value>`                  |
| **Error Rate**            | Percentage of failed requests                   | `<value>`                  |
| **Latency Percentiles**   | Response time for P90, P95, P99                 | `<values>`                 |
| **Burn Rate**             | Speed of error budget consumption               | `<value>`                  |
| **Throughput**            | Requests handled per second/minute/hour         | `<value>`                  |

---

## 5. Follow-Up
- **Preventive Measures**:
  - `<actions-to-prevent-recurrence>`
- **Monitoring Enhancements**:
  - `<improvements-to-alerting-or-monitoring>`
- **Documentation Updates**:
  - `<updates-to-runbooks-or-knowledge-bases>`
- **Review and Close**:
  - `<postmortem-meeting-summary>`

---

## 6. Recovery Objectives
| **Objective**               | **Definition**                                 | **Example**                |
|-----------------------------|------------------------------------------------|----------------------------|
| **RTO (Recovery Time Objective)** | Maximum acceptable downtime              | `<value>`                  |
| **RPO (Recovery Point Objective)** | Maximum acceptable data loss            | `<value>`                  |

---

## 7. Stakeholder Communication
- **Internal Communication**:
  - `<details-shared-with-teams>`
- **External Communication**:
  - `<customer-notifications-if-applicable>`

---

## 8. Lessons Learned
- **Key Insights**:
  - `<what-went-wrong-and-right>`
- **Process Improvements**:
  - `<suggestions-for-streamlining-incident-response>`
