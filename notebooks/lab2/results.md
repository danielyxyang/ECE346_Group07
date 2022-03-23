# ECE346 - Lab 2

## Task 1: Simulation Results

### A. Tuning of iLQR parameters
\#| \| |w_vel|w_contour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.891|*initial configuration (bypasses with 0.5)*
A1| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |24.998|*bypasses with 0.35, almost gets stuck*

<figure><img src="results_task1/base_snap.png" alt="base"><figcaption>base</figcaption></figure>
<figure><img src="results_task1/A1_snap.png" alt="A1"><figcaption>A1</figcaption></figure>

### B. Tuning of weights in cost
\#| \| |w_vel|w_contour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.891|*initial configuration (bypasses with 0.5)*
B1| \| |**10**|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.382|*bypasses with 0.7*
B2| \| |**20**|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.922|*bypasses with 0.8*
B3| \| |4|**15**|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |17.713|*bypasses with 0.6, drives more into the other lane*
B4*| \| |4|30|**4**|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |11.153|*brakes shortly, bypasses with 1.0*
B5| \| |4|30|0|**0**|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.059|*bypasses with 0.5, stays at slow speed a bit shorter*

<figure><img src="results_task1/base_snap.png" alt="base"><figcaption>base</figcaption></figure>
<figure><img src="results_task1/B1_snap.png" alt="B1"><figcaption>B1</figcaption></figure>
<figure><img src="results_task1/B2_snap.png" alt="B2"><figcaption>B2</figcaption></figure>
<figure><img src="results_task1/B3_snap.png" alt="B3"><figcaption>B3</figcaption></figure>
<figure><img src="results_task1/B4_snap.png" alt="B4"><figcaption>B4</figcaption></figure>
<figure><img src="results_task1/B5_snap.png" alt="B5"><figcaption>B5</figcaption></figure>

### C. Tuning of weights in soft constraint
\#| \| |w_vel|w_contour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.891|*initial configuration (bypasses with 0.5)*
C1| \| |4|30|0|0.1|0.1| \| |0 / 0|**1 / 4**|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |19.007|*bypasses with 0.5, cuts the curves a bit*
C2| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|**1 / 4**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |18.553|*bypasses with 0.7, comes very close to obstacle*

<figure><img src="results_task1/base_snap.png" alt="base"><figcaption>base</figcaption></figure>
<figure><img src="results_task1/C1_snap.png" alt="C1"><figcaption>C1</figcaption></figure>
<figure><img src="results_task1/C2_snap.png" alt="C2"><figcaption>C2</figcaption></figure>

### D. Joint tuning
\#| \| |w_vel|w_contour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.891|*initial configuration (bypasses with 0.5)*
D1| \| |**10**|30|0|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |25.303|*brakes down to 0.6, bypasses with 0.9*
D2| \| |**10**|30|**2**|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |12.833|*brakes shortly, bypasses with 1*
D3| \| |**10**|30|**4**|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |12.758|*constant speed of 1, drives badly on its lane*
D4| \| |**10**|**60**|**4**|0.1|0.1| \| |0 / 0|2 / 5|2 / 5|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |12.086|*constant speed of 1, drives well in its lane, comes close to obstacle*
D5*| \| |**10**|**60**|**4**|0.1|0.1| \| |0 / 0|2 / 5|**3 / 5.5**|1 / 5| \| |0|0|0|0| \| |**1.5**|**16**|50| \| |13.144|*brakes shortly, bypasses with 1, drives well in lane, keeps distance to obstacle*
D6*| \| |**10**|**60**|**4**|0.1|0.1| \| |0 / 0|2 / 5|**3 / 5.5**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |10.842|*brakes down to 0.8, bypasses with 1, drives well in lane, keeps distance to obstacle*

<figure><img src="results_task1/base.png" width="200" height="200" alt="base"><figcaption>base</figcaption></figure>
<figure><img src="results_task1/D1.png" width="200" height="200" alt="D1"><figcaption>D1</figcaption></figure>
<figure><img src="results_task1/D2.png" width="200" height="200" alt="D2"><figcaption>D2</figcaption></figure>
<figure><img src="results_task1/D3.png" width="200" height="200" alt="D3"><figcaption>D3</figcaption></figure>
<figure><img src="results_task1/D4.png" width="200" height="200" alt="D4"><figcaption>D4</figcaption></figure>
<figure><img src="results_task1/D5.png" width="200" height="200" alt="D5"><figcaption>D5</figcaption></figure>
<figure><img src="results_task1/D6.png" width="200" height="200" alt="D6"><figcaption>D6</figcaption></figure>

### Discussion
- `w_vel = 10` and `w_theta = 4`: provides incentives for the truck to be close to its maximum velocity and to increase its lap progress.
- `w_contour = 60`: prevents the truck from overly driving on the other lane and cutting the curves. However, this causes the truck to bypass the obstacle more closer than before, since the truck has to deviate from its reference trajectory.
- `q1_obstacle = 3` and `q2_obstacle = 5.5`: prevents the truck from bypassing the obstacle too close by making the barrier function more steep.

---------------

## Task 2: Simulation Results

The goal of tuning parameters is to shape the cost landscape on the track, such that iLQR can efficiently find an trajectory which is also reasonable in practice. Hence, good performance indicators for our parameters are
- **Planning time**: shorter planning time corresponds to less iLQR iterations indicating a more well-behaved cost landscape
- **Trajectory**: better trajectories corresponds to better match between cost landscape and desired behavior on the track

To describe the performance of our trajectory, we use the following terms to refer to particular stages of overtaking another truck:
- **Preparation (prep)**: The process of our truck changing to the second lane. 
- **Initiation (init)**: The process of our truck approaching the other truck on the second lane.
- **Overtaking**: The process of our truck bypassing the other truck.

### A. Tuning of iLQR parameters
*Note: Since the nominal trajectory of the other truck (task 1, experiment D6) only consists of `N = 11` planned states with a time horizon of `T = 1`, we have to use the same iLQR parameters for the planning of our truck.*

### B. Tuning of weights in cost
\#| \| |w_vel|w_countour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|40|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |13.828|*initial configuration (prep stable, init less stable, overtakes with 1.9)*
B1| \| |**8**|40|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |10.876|*prep instable, init stable, overtakes with 1.8*
B2a| \| |4|**80**|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |18.030|*not able to overtake*
B2b*| \| |4|**20**|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |10.513|*prep stable, init stable, overtakes with 1.8*
B3| \| |4|40|**4**|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.718|*prep less stable, init stable, overtakes with 1.9, hits the other truck shortly, cuts the curves heavily*
B4| \| |4|40|0|**0.5**|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |9.970|*prep almost stable, init less stable, overtakes with 1.5, requires more time to overtake, less deceleration*
B5| \| |4|40|0|0.1|**0.5**| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |10.934|*prep almost stable, init less stable, overtakes with 1.8, requires more time than base to plan maneuver*
B6| \| |**6**|40|**2**|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.666|*prep less stable, init stable, overtakes with 1.8*
B6b| \| |**6**|**20**|**2**|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.724|*?*
B7*| \| |**6**|40|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.334|*prep stable, init stable, overtakes with 1.9*
B7b| \| |**6**|**20**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |19.273|*?*

<figure><img src="results_task2/base.png" width="200" height="200" alt="base"><img src="results_task2/base_plan_snap.gif" width="200" height="200" alt="base_plan"><figcaption>base</figcaption></figure>
<figure><img src="results_task2/B1.png" width="200" height="200" alt="B1"><img src="results_task2/B1_plan_snap.gif" width="200" height="200" alt="B1_plan"><figcaption>B1</figcaption></figure>
<figure><img src="results_task2/B2a.png" width="200" height="200" alt="B2a"><img src="results_task2/B2a_plan_snap.gif" width="200" height="200" alt="B2a_plan"><figcaption>B2a</figcaption></figure>
<figure><img src="results_task2/B2b.png" width="200" height="200" alt="B2b"><img src="results_task2/B2b_plan_snap.gif" width="200" height="200" alt="B2b_plan"><figcaption>B2b</figcaption></figure>
<figure><img src="results_task2/B3.png" width="200" height="200" alt="B3"><img src="results_task2/B3_plan_snap.gif" width="200" height="200" alt="B3_plan"><figcaption>B3</figcaption></figure>
<figure><img src="results_task2/B4.png" width="200" height="200" alt="B4"><img src="results_task2/B4_plan_snap.gif" width="200" height="200" alt="B4_plan"><figcaption>B4</figcaption></figure>
<figure><img src="results_task2/B5.png" width="200" height="200" alt="B5"><img src="results_task2/B5_plan_snap.gif" width="200" height="200" alt="B5_plan"><figcaption>B5</figcaption></figure>
<figure><img src="results_task2/B6.png" width="200" height="200" alt="B6"><img src="results_task2/B6_plan_snap.gif" width="200" height="200" alt="B6_plan"><figcaption>B6</figcaption></figure>
<figure><img src="results_task2/B6b.png" width="200" height="200" alt="B6b"><img src="results_task2/B6b_plan_snap.gif" width="200" height="200" alt="B6b_plan"><figcaption>B6b</figcaption></figure>
<figure><img src="results_task2/B7.png" width="200" height="200" alt="B7"><img src="results_task2/B7_plan_snap.gif" width="200" height="200" alt="B7_plan"><figcaption>B7</figcaption></figure>
<figure><img src="results_task2/B7b.png" width="200" height="200" alt="B7b"><img src="results_task2/B7b_plan_snap.gif" width="200" height="200" alt="B7b_plan"><figcaption>B7b</figcaption></figure>

### C. Tuning of weights in soft constraint
\#| \| |w_vel|w_countour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|40|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |13.828|*initial configuration (prep stable, init less stable, overtakes with 1.9)*
C1| \| |4|40|0|0.1|0.1| \| |0 / 0|**3 / 10**|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |9.121|*prep stable, init less stable, overtakes with 1.9, bumps into track border few times*
C2| \| |4|40|0|0.1|0.1| \| |0 / 0|**3 / 5**|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |9.583|*prep less stable, init less stable, overtakes with 1.9, bumps into track border more heavily times*
C3*| \| |4|40|0|0.1|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |9.586|*prep stable, init stable, overtakes with 1.8, merges back earlier*
C4| \| |4|40|0|0.1|0.1| \| |0 / 0|5 / 10|**5 / 10**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |11.291|*prep stable, init less stable, overtakes with 1.8*
C5| \| |4|40|0|0.1|0.1| \| |0 / 0|**5 / 5**|**5 / 5**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |10.296|*prep instable, init instable, overtakes with 1.8, drives close to track border*

<figure><img src="results_task2/base.png" width="200" height="200" alt="base"><img src="results_task2/base_plan_snap.gif" width="200" height="200" alt="base_plan"><figcaption>base</figcaption></figure>
<figure><img src="results_task2/C1.png" width="200" height="200" alt="C1"><img src="results_task2/C1_plan_snap.gif" width="200" height="200" alt="C1_plan"><figcaption>C1</figcaption></figure>
<figure><img src="results_task2/C2.png" width="200" height="200" alt="C2"><img src="results_task2/C2_plan_snap.gif" width="200" height="200" alt="C2_plan"><figcaption>C2</figcaption></figure>
<figure><img src="results_task2/C3.png" width="200" height="200" alt="C3"><img src="results_task2/C3_plan_snap.gif" width="200" height="200" alt="C3_plan"><figcaption>C3</figcaption></figure>
<figure><img src="results_task2/C4.png" width="200" height="200" alt="C4"><img src="results_task2/C4_plan_snap.gif" width="200" height="200" alt="C4_plan"><figcaption>C4</figcaption></figure>
<figure><img src="results_task2/C5.png" width="200" height="200" alt="C5"><img src="results_task2/C5_plan_snap.gif" width="200" height="200" alt="C5_plan"><figcaption>C5</figcaption></figure>

### D. Joint tuning
\#| \| |w_vel|w_countour|w_theta|w_accel|w_delta| \| |q_v|q_road|q_obstacle|q_lat| \| |sig_x|sig_y|sig_v|sig_theta| \| |T|N|max_itr| \| |comp_time|remark
-| - |-|-|-|-|-| - |-|-|-|-| - |-|-|-|-| - |-|-|-| - |-|-
base| \| |4|40|0|0.1|0.1| \| |0 / 0|5 / 10|5 / 5|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |13.828|*initial configuration (prep stable, init less stable, overtakes with 1.9)*
D1| \| |**8**|40|0|0.1|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |11.291|*?*
D2| \| |4|40|**4**|0.1|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |13.634|*?*
D3| \| |**6**|40|**2**|0.1|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.477|*prep instable, init stable, overtakes with 1.9, merges back early*
D4| \| |**6**|40|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |14.229|*prep stable, init stable, overtakes with 1.9*
D5*| \| |**6**|**30**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.254|*prep stable, init stable, overtakes with 1.9, touches other truck and track border*
D6| \| |**2**|**30**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.124|*prep stable, init stable, overtakes with 1.7, does not touch other truck and track border*
D7| \| |**3**|**30**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.981|*prep stable, init stable, overtakes with 1.8, touches other truck very shortly*
D8| \| |**4**|**30**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |16.652|*prep stable, init stable, overtakes with 1.85, touches other truck and track border very shortly*
D9*| \| |**4**|**35**|**2**|**0.5**|0.1| \| |0 / 0|5 / 10|**3 / 6**|1 / 5| \| |0|0|0|0| \| |1|11|50| \| |15.748|*prep stable, init stable, overtakes with 1.75, does not touch other truck and track border*

<figure><img src="results_task2/base.png" width="200" height="200" alt="base"><img src="results_task2/base_plan_snap.gif" width="200" height="200" alt="base_plan"><figcaption>base</figcaption></figure>
<figure><img src="results_task2/D1.png" width="200" height="200" alt="D1"><img src="results_task2/D1_plan_snap.gif" width="200" height="200" alt="D1_plan"><figcaption>D1</figcaption></figure>
<figure><img src="results_task2/D2.png" width="200" height="200" alt="D2"><img src="results_task2/D2_plan_snap.gif" width="200" height="200" alt="D2_plan"><figcaption>D2</figcaption></figure>
<figure><img src="results_task2/D3.png" width="200" height="200" alt="D3"><img src="results_task2/D3_plan_snap.gif" width="200" height="200" alt="D3_plan"><figcaption>D3</figcaption></figure>
<figure><img src="results_task2/D4.png" width="200" height="200" alt="D4"><img src="results_task2/D4_plan_snap.gif" width="200" height="200" alt="D4_plan"><figcaption>D4</figcaption></figure>
<figure><img src="results_task2/D5.png" width="200" height="200" alt="D5"><img src="results_task2/D5_plan_snap.gif" width="200" height="200" alt="D5_plan"><figcaption>D5</figcaption></figure>
<figure><img src="results_task2/D6.png" width="200" height="200" alt="D6"><img src="results_task2/D6_plan_snap.gif" width="200" height="200" alt="D6_plan"><figcaption>D6</figcaption></figure>
<figure><img src="results_task2/D7.png" width="200" height="200" alt="D7"><img src="results_task2/D7_plan_snap.gif" width="200" height="200" alt="D7_plan"><figcaption>D7</figcaption></figure>
<figure><img src="results_task2/D8.png" width="200" height="200" alt="D8"><img src="results_task2/D8_plan_snap.gif" width="200" height="200" alt="D8_plan"><figcaption>D8</figcaption></figure>
<figure><img src="results_task2/D9.png" width="200" height="200" alt="D9"><img src="results_task2/D9_plan_snap.gif" width="200" height="200" alt="D9_plan"><figcaption>D9</figcaption></figure>

### Discussion
- `w_vel` and `w_theta` larger --> provides incentive for the truck to overtake the other truck (by allowing higher speeds), might regularize cost landscape to more efficient trajectories
- `w_vel` and `w_theta` not too large --> prevents truck to drive too aggressively (e.g. cutting curves, overtaking too closely)
- `w_contour` small --> provides incentive for the truck to overtake the other truck and to merge back later (by allowing larger deviations from reference track)
- `w_contour` not too small --> prevents truck to cut curves too aggressively
- `w_accel` larger --> might regularize cost landscape to trajectories with less acceleration and deceleration
- *`w_delta` larger --> might regularize cost landscape to more straight trajectories with less oscillations (??)*
- `q2_road <> q2_obstacle` (i.e. different rates of exponential increase for road and obstacle constraints) --> might reduce oscillations when computing the trajectory
- One can see significant decrease in computation time when tuning the barrier function parameters. This indicates that the cost landscape is more well-behaved when using tuned barrier functions.

The oscillation during initiation of the overtaking maneuver comes from the problem that in the beginning there is no explicit incentive for iLQR to find a trajectory such that the truck overtakes the other truck from the left side. Hence, the truck oscillates between overtaking from the right or left side until it gets close enough to the other truck.

### Further experiments
To analyze the generalization ability of the tuned parameters, we make the following experiments using the parameters D6 (a) and D9 (b):
1. Using right lane instead of center line as reference track for truck.
2. Using right lane and overtaking the other truck on a straight part of the track (`initial lap progress = 18`).
3. Using right lane and overtaking the other truck while the other truck bypasses the obstacle (`initial lap progress = 12`).

We observed that providing less incentive for overtaking the other truck (i.e. smaller `w_vel` and `w_theta`) to ensure a safer overtaking maneuver introduces major problems when overtaking from the right track instead of center line. One possible reason is the increased deviation from the reference line required for the overtaking maneuver, which increases the cost by `30 * 0.15 = 4.5`. To address this problem, one can use hybrid systems, which uses a the center line as reference track only for the overtaking maneuver.

<figure><img src="results_task2/E1a.png" width="200" height="200" alt="E1a"><img src="results_task2/E1a_plan.gif" width="200" height="200" alt="E1a_plan"><figcaption>E1a</figcaption></figure>
<figure><img src="results_task2/E1b.png" width="200" height="200" alt="E1b"><img src="results_task2/E1b_plan.gif" width="200" height="200" alt="E1b_plan"><figcaption>E1b</figcaption></figure>

<figure><img src="results_task2/E2a.png" width="200" height="200" alt="E2a"><img src="results_task2/E2a_plan.gif" width="200" height="200" alt="E2a_plan"><figcaption>E2a</figcaption></figure>
<figure><img src="results_task2/E2b.png" width="200" height="200" alt="E2b"><img src="results_task2/E2b_plan.gif" width="200" height="200" alt="E2b_plan"><figcaption>E2b</figcaption></figure>

<figure><img src="results_task2/E3a.png" width="200" height="200" alt="E3a"><img src="results_task2/E3a_plan.gif" width="200" height="200" alt="E3a_plan"><figcaption>E3a</figcaption></figure>
<figure><img src="results_task2/E3b.png" width="200" height="200" alt="E3b"><img src="results_task2/E3b_plan.gif" width="200" height="200" alt="E3b_plan"><figcaption>E3b</figcaption></figure>

### Further ideas
- The overtaking maneuver could be more safe when using a longer nominal trajectory of the other truck which would allow us to plan more ahead.


<style>
    figure {
        display: inline-block;
        margin: 0 0 5px 0;
    }
    figure > figcaption {
        text-align: center;
    }
</style>