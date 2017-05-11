function [result]=calculation(specread)
a=size(specread);
index=1;
counter=0;
for i=1:a(1):(a(1).*a(2)-39)
num=0;
counter=counter+1;
for j=i:1:i+39
if(specread(j)>40)
 num=10;
 endif
 endfor
if(num>0)
 result(index)=counter;
 index++;
 endif 
 endfor
 endfunction
