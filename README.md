# BSRA DAQ README

# Links
* [ipac24 indico](https://indico.jacow.org/)

# TODO
* create list of literature
* find examples of posters

# TIMBER VARIABLES AND TIMESTAMPS
* Date: 2023-10-24-19:50
    * LHC.BSRA.UA47.B1:VFC_ABORT_GAP_RAW_DATA_SPILL 
    * LHC.BSRA.US45.B1:ABORT_GAP_RAW_DATA_SPILL - 24/10

# NOTES
## Poster frames 
### Acquisition system
The DAQ is the core component of the AGM. It manages the timing of measurements, stores results, and sends it to the server regularly. The system stays synced with the TTC, receiving information about bunches and the start of each turn. The DAQ block diagram is shown in the picture on the right. The system captures incoming signals asynchronously and aligns them with the TTC by tagging samples with bunch and turn mark. Since data come from the ADC in blocks of 16x4 for each channel, bunch integrals are spread across 4 blocks, and the bunch start tag can appear on any of them. Because of this, they are first stored in the FIFO and then processed as a stream of samples.
The FIFO stores blocks containing samples from the acquisition window. This window is shifted by the bunch delay setting, determining the number of tags to ignore before initiating the writing procedure. Upon identifying the correct tag, it stores 400 blocks with bunch tag defining the region of interest. Those are transferred to the integration block. This block initiates integration at intervals of 100 ns (equivalent to 4 bunches) from the first appearance of the sample with a bunch tag and halts after generating 64 values. The memory linked to the integrator is utilized for compensating signal distortion caused by opening the gate of the MCP-PMT. The computed values undergo individual Exponential Moving Average (EMA) calculations. As a result of the filter feedback, its output incorporates all preceding results, reflecting the time evolution of the charge population within the 100ns intervals.
The outcomes are saved in the block RAM and transmitted via the VME64x bus. Whenever new data is available, the DAQ triggers an interrupt routine for the server, which retrieves the fresh measurements. Additionally, the system offers a VME64x to UART bridge for controlling the amplifier via the graphical client.

### amplifier
The amplifier is integrated into the OF, it is positioned near the MCP-PMT to minimize input noise before amplification, prior to transmission to the DAQ. The SL intensity varies depending on the particle beam type. 
To ensure full ADC resolution measurements despite the small signal magnitude, the amplifier gain range is within 41 dB and 87 dB. It features an adjustable offset ranging from -1V to 1V and an output LPF with a cutoff frequency of 40 MHz. Since strong light can harm the MCP-PMT, we keep its average cathode current below 100 mA. If it goes over this limit, an alarm built into the amplifier will be triggered. We can adjust all these settings using a simple UART interface, which is controlled by the DAQ.

### Instrument control
The DAQ and FO are 100 meters apart, requiring compensation for cable delays by adjusting the DAQ synchronization signal. A graphical client features this adjustment and verification of AGM outputs. The main window of the client depicted on the right shows three charts: raw data with estimated gate pulse position (top), AG population (middle left), and average population evolution over time (middle right). The left panel manages amplifier settings, while the bottom panel configures MCP-PMT voltage, optical filters, acquisition and gate delays. The remaining settings are for development purposes.

### system architecture
The OF, which includes a variable gain amplifier, is located at LHC Point 4 inside concrete shielding beneath the vacuum chamber. The system core is the DAQ, running on a standard CERN BI platform VFC-HD carrier. This platform connects an IAM ADC 500MSPS 14-bit FMC mezzanine digitizing the amplified MCP-PMT output. The amplifier is connected via UART and one signal for alarm sensing to the DAQ. There is an LED for AGM functionality verification during beam absence or calibration. The CERN BI multi-purpose Rear Transition Module (RTM) provides UART differential buffers, 15V gate level shifter and 30 mA LED current source. The entire system delivers measurements in regular intervals and is controled by the client through a VME64x bus.

### What is an abort gap monitor
The beam in the LHC can reach energies up to 350 MJ with a transverse size under 1 mm. This energy density can quench superconducting magnets. Therefore a beam dump system (BDS) handles beam extractions. Its kicker magnets divert the beam towards pits with graphite blocks for absorption. The beam bunch train is shown in the following figure. It includes a 3 μs Abort Gap (AG) to allow the kicker magnets to ramp up to their nominal field.
Particles can populate the Abort Gap (AG) due to various effects, and the accumulation of energy in this gap could lead to magnet quench during the beam dump process. Therefore, the AG is monitored using an Abort Gap Monitor (AGM).
The AGM is synchronized with the AG. It probes the AG in a non-invasive manner using OF, where a multi-channel photomultiplier (MCP-PMT) detects Synchrotron Light (SL). The acquisition window of the AGM is 6.4 μs long, providing sufficient time for the MCP-PMT gate to open and for the signal to return to the DAQ. The AG signal is 3 μs long, the rest is white noise. When the DAQ acquires the signal it divides it into 100 ns intervals and integrates the energy within each interval. This results in 64 values that are fed into the Exponential Moving Averager (EMA), which tracks the time evolution of charge within each interval.

### why we need new AGM
The current AGM, operational since 2010, utilizes the HAMAMATSU C5594 amplifier in the OF with a static gain of 36 dBV and a bandwidth ranging from 50 kHz to 1.5 GHz. The DAQ is implemented on the DAB64x platform, which incorporates the Altera Stratix EP1S40. Integration of the bunches is facilitated by the IBMS card, which embeds the ASIC lhcb2002b containing analog integrators. These integrators are synchronized with the LHC timing, integrating the charge within a single bunch and transmitting it to the DAQ. The DAQ aggregates 4 consecutive integrals to achieve intervals of 100 ns. In this manner, it generates 64 values and publishes them.
This system has limitations. The fixed gain of the amplifier reduces the resolution of digital conversion for lower SL intensities. The integrators have different gains and offsets requiring corrections within the DAQ. Finding the factors is challenging. Even after calibration, these negative effects are not eliminated entirely, resulting in residual artifacts in the output plots. To resolve these issues, the system needs to be moved to a different platform due to the obsoleted FPGA.

### results
The AGM gateware runs on the CERN BI standard platform with VFC-HD carrier and IAM ADC 500 MSPS 14-bit. This setup cuts down on maintenance expenses since the same hardware platform is used for multiple projects. 
The OF system is positioned adjacent to the current AGM at LHC point 4, sharing the same light source and utilizing 1/8 of its capacity (as shown in the figure in the top right corner). The update replaced the ASIC lhcb2002b with a variable gain amplifier. Initial data measurements have been taken since September 2023 on an ion beam. The snapshot of plots is displayed in the figure on the right, with the red curve representing measurements from the current AGM and the blue curve corresponding to the updated AGM. The valid signal falls between interval indices 16 and 48, which aligns with the opening of the MCP-PMT gate. Any signal outside this gate is expected to be white noise. The peak observed at index 47 represents the tail of the first bunch in the bunch train.
A deviation chart has been generated for comparing the two plots, shown as the yellow curve, with the current AGM as the reference. The deviation peak is observed in the region where white noise is expected to be measured, but it is distorted by the ASIC. However, the blue plot behaves as expected, indicating that the new AGM has successfully eliminated artifacts from the output plots.
