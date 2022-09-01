# Forwarding_Engine_Drops 
How to get forwarding engine drops for each port. 

There are many reasons that forwarding engine drops are generated under a specific port: 

- Malformed IP header
- IP SA or DA not valid
- Service MTU exceeded
- SAP or SDP or service disabled
- Ethertype or PPP ID unknown
- Interface disabled
- MAC DA not our interface MAC
- Same segment discard
- Bad checksum
- TTL expired

After the code runs:

<img width="367" alt="Working_after_the_code_runs" src="https://user-images.githubusercontent.com/94804863/162370704-fbef6af4-991d-48e1-ba09-0dc8d63c947b.PNG">

<img width="345" alt="Error_after_the_code_runs" src="https://user-images.githubusercontent.com/94804863/162370717-fa86a052-e47e-4d0e-b402-ef3481c962f3.PNG">
