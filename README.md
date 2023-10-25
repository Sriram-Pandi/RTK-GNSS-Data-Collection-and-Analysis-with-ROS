**RTK GNSS Data Collection and Analysis with ROS**

This project revolves around the acquisition and analysis of data using RTK (Real-Time Kinematics) GNSS (Global Navigation Satellite System) equipment. Through the Robot Operating System (ROS), I established a system with the following features:

1. **RTK GNSS Driver Development**: I adapted the GNSS driver from Lab 1 to cater to the new NMEA string, ‘GNGGA’. Alongside this, the driver was enhanced to include the GNSS fix quality (either rtk float or rtk fix) which would play a crucial role in the subsequent analysis.

2. **Hardware Configuration**: The hardware setup consisted of:
   - 2 RTK processing boards.
   - 2 GNSS antennas.
   - 2 telemetry radios operating at 915 MHz.
   Special care was taken to follow the setup instructions precisely, ensuring the base RTK remained stationary, sending corrections to the rover over radio. The laptop was connected to the rover via a usb-serial connection to receive the corrected GNSS fix solution in the NMEA format.

3. **Data Collection**:
   - Stationary Data: After setting up the RTK pair in an open area, I collected a stationary dataset for 10 minutes.
   - Structured Movement: Another dataset was taken with the rover moving in a predetermined path, ensuring it returned to its initial position and orientation.
   - Varied Environment Data: Two additional datasets (stationary and moving rover) were captured in locations with partial occlusions and reflections.

4. **Data Analysis**:
   - Through plotting and statistics, I analyzed the UTM data derived from each dataset.
   - The analysis shed light on the efficacy and accuracy of RTK GNSS navigation, specifically the error estimates.
   - I also delved deep into understanding the noise distribution in the signal, which holds implications for real-world navigation scenarios.

5. **Documentation**: I meticulously documented the findings in a comprehensive report, detailing the methods, observations, and inferences. This report was designed to be easily interpretable, backed by visual aids and concise explanations.

6. **Repository Structure**: I've organized my GitHub repository to ensure ease of access and clarity. The structure includes separate directories for ROS drivers, data analysis scripts, and the final report.

By the end of this project, I gained profound insights into the workings of RTK GNSS systems, understanding both their potential and the challenges they present in real-world navigation scenarios.
