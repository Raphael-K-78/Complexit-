function [PGCD,PPCM] = euclide(a,b)
%EUCLIDE Summary of this function goes here
%   Detailed explanation goes here
temp2 = b;
temp3 = a;
while temp2 ~= 0
    temp = b;
    temp2 = mod(temp3, temp2);
    temp3 = temp;
end
PGCD = temp3;
PPCM = (a * b) / PGCD;
end