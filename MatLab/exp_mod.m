function [res] = exp_mod(a,b,n)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    res = 1;
    bbin = dec2bin(b);
    rbbin = fliplr(bbin);
    for i = 1:length(bbin)
        if i == 1
            val = mod(a,n);
        else
            val = mod(val^2,n);
        end
        if bbin( length(bbin) - i+1) == '1'
            res = mod((res * val) ,n);
        end
    end
end