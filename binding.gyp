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
                "/home/pi/Desktop/dbr/include"
            ],
            'libraries': [
                "-lDynamsoftBarcodeReader", "-L/home/pi/Desktop/dbr/lib"
            ]
          }]
      ]
    }
  ]
}
