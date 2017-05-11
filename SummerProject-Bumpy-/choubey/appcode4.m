clear all;
close all;
format long;
[Ltime,date,latitude,longitude,x,y,z]=textread("read.txt","%f %f %f %f %f %f %f");
fs=40;
X=x.*x;
Y=y.*y;
Z=z.*z;


time=[1/40:1/40:1/40*size(X)];
time=ctranspose(time);

amplitude=sqrt(X+Y+Z);

amplitude=abs(amplitude-mean(amplitude));
for i=1:1:size(amplitude)
if(amplitude(i)<2.5)
amplitude(i)=0;
endif
endfor

pkg load signal
graphics_toolkit fltk
s=abs(specgram(amplitude,80,40))

fresult=calculation(s);
track=size(fresult);
ind=0;
for i=1:1:track(2)
ind++;
latresult(ind)=mean(latitude(fresult(i).*fs-20):latitude(fresult(i).*fs+20));
longresult(ind)=mean(longitude(fresult(i).*fs-20):longitude(fresult(i).*fs+20));
endfor
finalstorage=[ctranspose(latresult) ctranspose(longresult)];
save locations.mat finalstorage
