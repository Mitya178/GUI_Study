



# GUI_Study
Studing gui add inside a docker container

## Linux
```
Check:How work your app with python on Linux:
# python3 <Name_YOUR_app>
```

## Docker
```
#Before work:check Dockerfile(CMD)

# docker build -t <Name_YOUR_app>:(version).

#xhost +si:localuser:root        VERY IMPORTANT THING

#xhost +local:                   VERY IMPORTANT THING

# docker tag <Name_YOUR_app>:(version) mitya178/<Name_YOUR_app>:(version)

# docker push mitya178/<Name_YOUR_app>:(version)

# docker pull mitya178/<Name_YOUR_app>:(version)

# docker run -it --rm -e DISPLAY=:"0" -v /tmp/.X11-unix:/tmp/.X11-unix --name <Name_YOUR_container> <Name_YOUR_app>:(version)
```


## Support
```
# Operation system:Debian 11
```
