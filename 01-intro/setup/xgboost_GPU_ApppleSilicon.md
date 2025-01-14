# Building XGBoost with GPU Support

By default, XGBoost is built without GPU support. To build XGBoost with GPU support, you will need to modify the build configuration. The following steps will guide you through the process of building XGBoost with GPU support on the M1 Pro chipset.

1. Clone the XGBoost repository:

```bash
git clone --recursive <https://github.com/dmlc/xgboost>
```

2. Change to the XGBoost directory:

```bash
cd xgboost
```

3. Modify the build configuration:

```bash
cp make/minimum.mk config.mksed -i '' 's/^CXX =.*/CXX = clang++/' config.mksed -i '' 's/^CC =.*/CC = clang/' config.mksed -i '' 's/^USE_OPENMP =.*/USE_OPENMP = 0/' config.mksed -i '' 's/^CMAKE_PREFIX_PATH =.*/CMAKE_PREFIX_PATH = /usr/local/' config.mksed -i '' 's/^CMAKE_OSX_SYSROOT =.*/CMAKE_OSX_SYSROOT = macosx/' config.mksed -i '' 's/^CMAKE_CXX_FLAGS =.*/CMAKE_CXX_FLAGS = -march=native -mtune=native -I/usr/local/include -I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/' config.mksed -i '' 's/^CMAKE_C_FLAGS =.*/CMAKE_C_FLAGS = -march=native -mtune=native -I/usr/local/include -I/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/' config.mk
```

4. Build XGBoost with GPU support:

```bash
make -j$(sysctl -n hw.physicalcpu) USE_CUDA=1
```

Once XGBoost is built with GPU support, you can use it to accelerate your machine learning applications on the M1 Pro chipset.

In this article, we discussed how to enable GPU XGBoost on Apple's M1 Pro chipset for faster training. By following the steps outlined in this article, you can take advantage of the M1 Pro chipset's powerful GPU to significantly reduce training times for your machine learning applications.

[Source](https://devcodef1.com/news/1136152/gpuxgboost-on-m1-pro)