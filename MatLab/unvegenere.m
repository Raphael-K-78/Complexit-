function [texte] = unvegenere(code,key)
    code = lower(code);
    key  = lower(key);

    sizeCode = length(code);
    sizeKey = length(key);

    if sizeKey > sizeCode %key trop grand
        key = key(1:sizeCode);
    elseif sizeKey < sizeCode % si key trop petit
        key = repmat(key, 1, ceil(sizeCode / sizeKey));
        key = key(1:sizeCode);
    end

    texte = char(mod( (code - 97) - (key - 97), 26 ) + 97);
end
