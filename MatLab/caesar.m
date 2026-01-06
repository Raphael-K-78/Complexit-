function [texte] = caesar(code,key)
%CAESAR Summary of this function goes here
%   Detailed explanation goes here
    texte =char(mod((code - 97) + key,26)+97);
    %decode = code - 97;
    %decode = decode + key;
    %decode = mod(decode,26);
    %texte = char(decode + 97);
end
