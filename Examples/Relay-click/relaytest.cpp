/*
*	Relay Test example application
*
* Written by Peter Szamosi <szamosi.peter@gmail.com>
*
*	This application is for use with the Relay Click board specific dtbo file in place /lib/firmware/
*
* Using SimpleGPIO.h and SimpleGPIO.cpp written by Derek Molly ->  derekmolly.ie
*
*
*/



#include <iostream>
#include <string>
#include <unistd.h>
#include "SimpleGPIO.h"
using namespace std;

unsigned int RL1 = 50;   // Relay RL1 GPIO1_18
unsigned int RL2 = 113;   // Relay RL2 GPIO3_17

int main(int argc, char *argv[]){
	
	cout << "Setting GPIO Pins" << endl;
        gpio_export(RL1); 	// Relay 1 (RL1)
		gpio_export(RL2);   // Relay 2 (RL2)
        gpio_set_dir(RL1, OUTPUT_PIN);   // RL1 is set as an output
		gpio_set_dir(RL2, OUTPUT_PIN);   // RL2 is set as an output
	
	//Switch the Relays on and off 3 times one after the other
	for(int i=0; i<5; i++){
	cout << "RL1 on" << endl;
		gpio_set_value(RL1, HIGH);
		usleep(100000);				// on for 100ms
	cout << "RL1 off RL2 on" << endl;
		gpio_set_value(RL1, LOW);
		gpio_set_value(RL2, HIGH);
		usleep(100000);				// on for 100ms
	cout << "RL2 off" << endl;
		gpio_set_value(RL2, LOW);
		
	}
	cout << "done" << endl;
	gpio_unexport(RL1);     // unexport the LED
	gpio_unexport(RL2);  // unexport the push button
	cout << "exiting" << endl;
	return 0;
}