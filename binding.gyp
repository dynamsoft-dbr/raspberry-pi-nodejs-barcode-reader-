{
  "targets": [
    {
      'target_name': "dbr",
      'sources': [ "dbr.cc" ],
      'conditions': [
          ['OS=="linux"', {
            'defines': [
              'LINUX_DBR',
            ],
            'include_dirs': [
                "/home/pi/dbr-V4.2.0-linux-armv7l/include"
            ],
            'libraries': [
                "-lDynamsoftBarcodeReader", "-L/home/pi/dbr-V4.2.0-linux-armv7l/lib"
            ]
          }]
      ]
    }
  ]
}
