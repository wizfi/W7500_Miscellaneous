#ifndef XMODEM_H_
#define XMODEM_H_

#include "type.h"
#include "uart.h"

#define SOH  0x01
#define STX  0x02
#define EOT  0x04
#define ACK  0x06
#define NAK  0x15
#define CAN  0x18
#define CTRLZ 0x1A

//#define DLY_1S 10000000
#define DLY_1S 100000
#define MAXRETRANS 25

#define XMDM_SRAM	0
#define XMDM_FLSH	1


int xmodemReceive(unsigned char *dest, int destsz, int opt);

#endif	/* XMODEM_H_ */
