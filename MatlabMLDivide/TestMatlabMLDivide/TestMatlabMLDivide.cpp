// TestMatlabMLDivide.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;

#include "matlab_mldivide.h"

#include "matlab_mldivide_emxAPI.h"


int main()
{
	cout << "Hell yeah!" << endl;

	int a_size[2] = { 3, 3 };
	emxArray_creal_T* a_array = emxCreateND_creal_T(2, a_size);

	int b_size[2] = { 3, 1 };
	emxArray_creal_T* b_array = emxCreateND_creal_T(2, b_size);

	int c_size[2] = { 3, 1 };
	emxArray_creal_T* c_array = emxCreateND_creal_T(2, c_size);

	int a_data[9] = { 8, 1, 6, 3, 5, 7, 4, 9, 2 };

	for(int i = 0; i < 9; i++)
	{
		a_array->data[i].re = a_data[i];
	}

	int b_data[3] = {15, 15, 15};

	for(int i = 0; i < 3; i++)
	{
		b_array->data[i].re = b_data[i];
	}


	matlab_mldivide(a_array, b_array, c_array);
	for(int i = 0; i < 3; i++)
		cout << c_array->data[i].re << endl;

	return 0;
}

