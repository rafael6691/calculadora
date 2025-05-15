function Q = trapecio(c, v, a, b)
    x = linspace(a, b, length(c));
    Q = trapz(x, c .* v);
end
