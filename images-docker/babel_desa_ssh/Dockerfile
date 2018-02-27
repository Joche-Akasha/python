FROM aka/babel-desa

RUN apt-get install -y openssh-server

#ssh
RUN useradd usu1
RUN mkdir /var/run/sshd
RUN echo 'usu1:usu1' | chpasswd

#Startup
RUN /etc/init.d/ssh start 
EXPOSE 22 

