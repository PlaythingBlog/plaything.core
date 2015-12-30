apt-get install libxslt-dev libxml2-dev -y

INSTALLERFILE=Plone-5.0-UnifiedInstaller-r1.tgz
INSTALLERFOLDER=Plone-5.0-UnifiedInstaller-r1
INSTALLERURL=https://launchpad.net/plone/5.0/5.0/+download/Plone-5.0-UnifiedInstaller-r1.tgz

echo "----> setting up buildout defaults"
mkdir $HOME/.buildout
wget https://raw.githubusercontent.com/pndk/installerscripts/master/c9.buildout.defaults.cfg -O $HOME/.buildout/default.cfg


spinner()
{
    local pid=$1
    local delay=0.75
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

echo "getting the installer"
if [ -s $INSTALLERFILE ]  
then  
    echo "----> We already have the installer file"
else  
    echo "----> Downloading the installer file"
    wget $INSTALLERURL &
    spinner $!
fi
echo "----> unpacking the installer"
tar xfz $INSTALLERFILE

mv $INSTALLERFOLDER/packages/buildout-cache.tar.bz2 .
tar xfj buildout-cache.tar.bz2
mkdir -p buildout-cache/extends

echo "----> starting installation"
python bootstrap-buildout.py &
spinner $!
bin/buildout &
spinner $!udo apt-get install libxslt-dev libxml2-dev -y

INSTALLERFILE=Plone-5.0-UnifiedInstaller-r1.tgz
INSTALLERFOLDER=Plone-5.0-UnifiedInstaller-r1
INSTALLERURL=https://launchpad.net/plone/5.0/5.0/+download/Plone-5.0-UnifiedInstaller-r1.tgz

echo "----> setting up buildout defaults"
mkdir $HOME/.buildout
wget https://raw.githubusercontent.com/pndk/installerscripts/master/c9.buildout.defaults.cfg -O $HOME/.buildout/default.cfg


spinner()
{
    local pid=$1
    local delay=0.75
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

echo "getting the installer"
if [ -s $INSTALLERFILE ]  
then  
    echo "----> We already have the installer file"
else  
    echo "----> Downloading the installer file"
    wget $INSTALLERURL &
    spinner $!
fi
echo "----> unpacking the installer"
tar xfz $INSTALLERFILE

mv $INSTALLERFOLDER/packages/buildout-cache.tar.bz2 .
tar xfj buildout-cache.tar.bz2
mkdir -p buildout-cache/extends

echo "----> starting installation"
python bootstrap-buildout.py &
spinner $!
bin/buildout &
spinner $!

echo "----> setting up a Plaything site"
bin/instance run scripts/addPloneSite.py plaything
