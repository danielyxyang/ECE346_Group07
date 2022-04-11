# ECE346 - Lab 2

## Task 2: Simulation Results

### A. Results under ideal observations
In this experiment, our own truck always observes the true state. Hence, the belief about the state of the other truck increases monotonically for the true state.

\#| \| |(G1, forward)|(G2, forward)|(G1, stop)|(G2, stop)| \| |forward|stop| \| |remark
-| - |-|-|-|-| - |-|-| - |-
A0| \| |[0.8, 0.2]|[0.1, 0.9]|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|[-1, -1]| \| |
A1| \| |**[0.9, 0.1]**|**[0.6, 0.4]**|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|[-1, -1]| \| | *less conservative (more prob. on s' = G1)*
A2| \| |**[0.9, 0.1]**|**[0.9, 0.1]**|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|[-1, -1]| \| | *less conservative (more prob. on s' = G1)*
A3| \| |**[0.9, 0.1]**|**[0.9, 0.1]**|[0.5, 0.5]|[0.05, 0.95]| \| |**[10, -10]**|[-1, -1]| \| | *collision (more prob. on s' = G1, higher reward for forward)*
A4| \| |**[0.9, 0.1]**|**[0.9, 0.1]**|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|**[-14, -14]**| \| | *almost collision (more prob. on s' = G1, smaller reward for stop)*

A0:
<img src="results_task2/A0_0.gif" width="200" alt="A0_0"><img src="results_task2/A0_0_pdf.gif" width="200" alt="A0_0_pdf">
<img src="results_task2/A0_1.gif" width="200" alt="A0_1"><img src="results_task2/A0_1_pdf.gif" width="200" alt="A0_1_pdf">

A1:
<img src="results_task2/A1_0.gif" width="200" alt="A1_0"><img src="results_task2/A1_0_pdf.gif" width="200" alt="A1_0_pdf">
<img src="results_task2/A1_1.gif" width="200" alt="A1_1"><img src="results_task2/A1_1_pdf.gif" width="200" alt="A1_1_pdf">

A2:
<img src="results_task2/A2_0.gif" width="200" alt="A2_0"><img src="results_task2/A2_0_pdf.gif" width="200" alt="A2_0_pdf">
<img src="results_task2/A2_1.gif" width="200" alt="A2_1"><img src="results_task2/A2_1_pdf.gif" width="200" alt="A2_1_pdf">

A3:
<img src="results_task2/A3_0.gif" width="200" alt="A0_3"><img src="results_task2/A3_0_pdf.gif" width="200" alt="A0_3_pdf">
<img src="results_task2/A3_1.gif" width="200" alt="A0_3"><img src="results_task2/A3_1_pdf.gif" width="200" alt="A0_3_pdf">

A4:
<img src="results_task2/A4_0.gif" width="200" alt="A0_4"><img src="results_task2/A4_0_pdf.gif" width="200" alt="A0_4_pdf">
<img src="results_task2/A4_1.gif" width="200" alt="A0_4"><img src="results_task2/A4_1_pdf.gif" width="200" alt="A0_4_pdf">

### B. Results under more realistic observations
In this experiment, we randomize the observations of our own truck and increase the probability of observing the true state over time. This increases the uncertainty in the belief about the state of the other truck.

\#| \| |(G1, forward)|(G2, forward)|(G1, stop)|(G2, stop)| \| |forward|stop| \| |remark
-| - |-|-|-|-| - |-|-| - |-
B0| \| |[0.8, 0.2]|[0.1, 0.9]|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|[-1, -1]| \| | *too conservative, does not move (higher uncertainty for s' = G1)*
B1| \| |[0.8, 0.2]|[0.1, 0.9]|[0.5, 0.5]|[0.05, 0.95]| \| |**[10, -50]**|[-1, -1]| \| | *conservative, starts moving very late*
B2| \| |[0.8, 0.2]|[0.1, 0.9]|[0.5, 0.5]|[0.05, 0.95]| \| |**[10, -10]**|[-1, -1]| \| | *almost collision*
B3| \| |[0.8, 0.2]|[0.1, 0.9]|[0.5, 0.5]|[0.05, 0.95]| \| |[10, -100]|**[-14, -14]**| \| | *less conservative, starts moving earlier*

B0:
<img src="results_task2/B0_0.gif" width="200" alt="B0_0"><img src="results_task2/B0_0_pdf.gif" width="200" alt="B0_0_pdf">
<img src="results_task2/B0_1.gif" width="200" alt="B0_1"><img src="results_task2/B0_1_pdf.gif" width="200" alt="B0_1_pdf">

B1:
<img src="results_task2/B1_0.gif" width="200" alt="B1_0"><img src="results_task2/B1_0_pdf.gif" width="200" alt="B1_0_pdf">
<img src="results_task2/B1_1.gif" width="200" alt="B1_1"><img src="results_task2/B1_1_pdf.gif" width="200" alt="B1_1_pdf">

B2:
<img src="results_task2/B2_0.gif" width="200" alt="B2_0"><img src="results_task2/B2_0_pdf.gif" width="200" alt="B2_0_pdf">
<img src="results_task2/B2_1.gif" width="200" alt="B2_1"><img src="results_task2/B2_1_pdf.gif" width="200" alt="B2_1_pdf">

B3:
<img src="results_task2/B3_0.gif" width="200" alt="B0_3"><img src="results_task2/B3_0_pdf.gif" width="200" alt="B0_3_pdf">
<img src="results_task2/B3_1.gif" width="200" alt="B0_3"><img src="results_task2/B3_1_pdf.gif" width="200" alt="B0_3_pdf">