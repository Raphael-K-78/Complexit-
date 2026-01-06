function [fibo] = fibonacciV2(u)
    if u==0 || u==1
        fibo = 1;
    elseif u<5
    else
        fibo = fibonacciV2(u - 1) + fibonacciV2(u - 2);
    end
end