function Q = simpson(c, v, a, b)
    x = linspace(a, b, length(c));
    y = c .* v;
    n = length(x);
    if mod(n,2) == 0
        n = n-1;
        x = x(1:n);
        y = y(1:n);
    end
    h = (b - a) / (n - 1);
    Q = y(1) + y(n) + 4 * sum(y(2:2:end-1)) + 2 * sum(y(3:2:end-2));
    Q = Q * h / 3;
end
