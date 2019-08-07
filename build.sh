ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "2" ]; then
    echo "pac-abe requires python2"
    exit 1
fi

git submodule update --init
cd dash_hash
python2 setup.py install
cd ..
python2 setup.py install
