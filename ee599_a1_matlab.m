clc
clear

% Read
[y_full,fs] = audioread('Samples/sarigamapa.wav');

% Parameters
win_size = fs*0.25;
win_gap = fs*0.05;
win_count = floor((length(y_full)-win_size)/win_gap);
pole_count = 128;

% Analysis
pitch = zeros(win_count,1);
yhat = zeros(win_count*win_size,1);
fpoles = zeros(pole_count,1);
for i = 0:win_count-1
    y = y_full(i*win_gap + 1: i*win_gap + win_size);
    [a,e] = lpc(y,pole_count);
    x = zeros(win_size,1);
    x(1) = 1;
    yhat(i*win_gap + 1: i*win_gap + win_size) = filter(1,a,x);  
    fpoles_temp = fs*sort(abs(angle(roots(a))))/(2*pi);
    fpoles_temp = fpoles_temp(fpoles_temp ~= 0);
    pitch(i+1) = fpoles_temp(1);
end

% Figures
figure(1)
bar(a)
% figure(2)
% stem(x)
figure(3)
plot(yhat)
% figure(4)
% stem(fpoles)
figure(5)
plot(pitch)