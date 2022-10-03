# XenusControll
 
| Code |  Command   |                           Description                           |
|:----:|:----------:|:---------------------------------------------------------------:|
|  s   |    Set     |             Set a value a parameter in ram or flash             |
|  g   |    Get     |          Read the value of a parameter in ram or flash          |
|  c   |    Copy    | Copy the value of a parameter from ram to flash or flash to ram |
|  r   |   Reset    |                         Reset the drive                         |
|  t   | Trajectory |                  Trajectory generator command                   |
|  i   |  Register  |        Read or write the value of a CVM program register        |

# 2.2 Page 10. Set Command(s)

The s command is used to set the value of a drive parameter in RAM or flash.
## Syntax

[node ID][<.>axis letter] s [memory bank][parameter ID] [value]<CR>

## Command Specific Parameters


| Command |  Response   |                           Comment                           |
|:----:|:----------:|:---------------------------------------------------------------:|
|  s r0x30 1200   |    ok     |             Set parameter 0x30 (position loop proportional gain) to 1200 in RAM. The “ok” response indicates that the command executed successfully.             |
|  s f0x30 1200   |    ok     |          Set parameter 0x30 (position loop proportional gain) to 1200 in flash. The “ok” response indicates that the command executed successfully.          |
|  3 s f0x30 1200   |    ok    | Set parameter 0x30 (position loop proportional gain) to 1200 in flash for the drive with CAN node ID of 3. The “ok” response indicates that the command executed successfully. |
|  .b s f0x30 1200   |   ok    |                         Set parameter 0x30 (position loop proportional gain) to 1200 in flash on axis B. The “ok” response indicates that the command executed successfully.                         |
|  s r 0x30 1000   | e 33 |                  Attempted to set 0x30 to 1200 in RAM. Error 33 (ASCII command parsing error) was returned. Note the extra space between the bank and the parameter ID.                   |

# 2.3 Page 11. Get Command (g)
The g command is used to read the value of a drive parameter from RAM or flash.

## Syntax
[node ID][<.>axis letter] g [memory bank][parameter ID][optional <x>]<CR>

| Command |  Response   |                           Comment                           |
|:----:|:----------:|:---------------------------------------------------------------:|
|  g r0x30   |    v 1200     |             Read the value of parameter 0x30 (position loop proportional gain) from RAM. Example shows a value of 1200 returned.             |
|  3 g r0x30   |    v 1200     |          Read the value of parameter 0x30 (position loop proportional gain) from RAM for the drive with CAN node ID of 3. Example shows a value of 1200 returned.          |
|  .b g r0x30   |    v 1200    | Read the value of parameter 0x30 (position loop proportional gain) from RAM on axis B. Example shows a value of 1200 returned. |
|  g r0xa0x   |   v 0x4000f800    |                         Read the value of parameter 0xa0 (amplifier event status) and return the value in hexadecimal format.                         |
|  g f0x17   | e 15 |                  Attempted to read parameter 0x17 (actual motor position) from flash. Error 15 (Parameter doesn’t exist on requested page) was returned. Note that actual motor position is stored in RAM only.                   |

# 2.4: Copy Command (c)
The c command is used to copy the value of a parameter from one memory bank to another (RAM to flash or flash to RAM).
## Syntax
[node ID][<.>axis letter] c [memory bank][parameter ID]<CR>

| Command |  Response   |                           Comment                           |
|:----:|:----------:|:---------------------------------------------------------------:|
|  c r0x30   |    ok     |             Copy the value of 0x30 from RAM to flash. The “ok” response indicates that the command executed successfully.             |
|  .b c r0x30   |    ok     |          Copy the value of 0x30 from RAM to flash for axis B. The “ok” response indicates that the command executed successfully.          |
|  3 c r0x30   |    ok    | Copy the value of 0x30 from RAM to flash for the drive with CAN node ID of 3. The “ok” response indicates that the command executed successfully. |
|  c f0x30   |   ok    |                         Copy the value of 0x30 from flash to RAM. The “ok” response indicates that the command executed successfully.                        |

# 2.5: Reset Drive Command (r)
The r command is used to reset the drive. The command requires no additional parameters. The drive baud rate is set to 9600 when the drive restarts. The drive does not respond to this message.
NOTE: if a reset command is issued to a drive on a multi-drop network, error code 32, “CAN Network communications failure,” will be received. This is because the drive reset before responding to the gateway drive. In this case, the error can be ignored.

## Syntax
[optional node ID] r<CR>
## Notes
The axis letter has no effect with this command because the reset command applies to all axes of a multi-axis drive.

|  Command   |  Response   |                           Comment                           |
|:----------:|:----------:|:---------------------------------------------------------------:|
|     r      |    none     |             Drive is reset.             |
| 3 r |    none     |          The drive with CAN node ID of 3 is reset.          |