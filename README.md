# conan-tiny-dnn

![conan-tiny-dnn image](/images/conan-tiny-dnn.png)

[![Download](https://api.bintray.com/packages/conan-community/conan/tiny-dnn%3Aconan/images/download.svg?version=0.1.1%3Astable)](https://bintray.com/conan-community/conan/tiny-dnn%3Aconan/0.1.1%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-tiny-dnn.svg?branch=stable%2F0.1.1)](https://travis-ci.org/conan-community/conan-tiny-dnn)

[Conan.io](https://conan.io) package for [MiLi](https://bitbucket.org/fudepan/tiny-dnn/overview) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/tiny-dnn%3Aconan).

## Basic setup

    $ conan install tiny-dnn/0.1.1@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    tiny-dnn/0.1.1@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)