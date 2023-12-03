# Maintainer: Ignacio Jimenez <linyers666 [at] gmail [dot] com>

pkgname=pydoli
pkgver=0.1
pkgrel=1
pkgdesc='A simple todo list app for the command line'
url='https://github.com/linyers/pydoli'
arch=('any')
license=('MIT')
depends=('python>=3.6', 'pydoli')


build() {
    cd $pkgname-$pkgver
    python setup.py build
}

package() {
	cd $pkgname-$pkgver
	python setup.py install --prefix=/usr --root="${pkgdir}" -O1 --skip-build
	install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
	install -Dm 644 README.md -t "${pkgdir}"/usr/share/doc/${pkgname}
}