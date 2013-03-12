from distutils.core import setup, Extension

pkg = 'Extensions.OnDemand'
setup (name = 'enigma2-plugin-extensions-ondemand',
       version = '0.1',
       license='GPLv2',
       url='git://github.com/E2OpenBhPlugins/OnDemand.git',
       description='On Demand',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data={pkg: ['*.png', 'LICENS*' 'icons/*.png']}
      )
