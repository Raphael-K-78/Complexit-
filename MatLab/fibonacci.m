function [u2] = fibonacci(u)
    u0 = 0;
    u1 = 1;
    u2 = 0;
    for index = 2:u
        u2 = u1 + u0;
        u0 = u1;
        u1 = u2;
    end
end