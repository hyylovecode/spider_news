mv src src-back
mkdir src
cp src-back/*.txt src/
cp src-back/*.sh src/
cp src-back/*.py src/
cd src
rm typing_extensions.py
rm dataclasses.py
chmod +x install.sh
./install.sh
cd ..

