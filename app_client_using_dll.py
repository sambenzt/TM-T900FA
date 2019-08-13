
# It requires pywin32:  https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/
#
# Note: windll use by default the calling convention "StdCall"

from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer
import binascii
import sys
from ctypes import windll


# -----------------------------------------------------------------------------
# GLOBAL DEFINES AREA
# -----------------------------------------------------------------------------
ID_TIPO_COMPROBANTE_TIQUET                = 1   # "83"  Tique
ID_TIPO_COMPROBANTE_TIQUE_FACTURA         = 2   # "81"  Tique Factura A, "82" Tique Factura B, "111" Tique Factura C, "118" Tique Factura M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO = 3   # "110" Tique Nota de Credito, "112" Tique Nota de Credito A, "113" Tique Nota de Credito B, "114" Tique Nota de Credito C, "119" Tique Nota de Credito M
ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO  = 4   # "115" Tique Nota de Debito A, "116" Tique Nota de Debito B, "117" Tique Nota de Debito C, "120" Tique Nota de Debito M

ID_TIPO_DOCUMENTO_NINGUNO           = 0
ID_TIPO_DOCUMENTO_DNI               = 1
ID_TIPO_DOCUMENTO_CUIL              = 2
ID_TIPO_DOCUMENTO_CUIT              = 3
ID_TIPO_DOCUMENTO_CEDULA_IDENTIDAD  = 4
ID_TIPO_DOCUMENTO_PASAPORTE         = 5
ID_TIPO_DOCUMENTO_LIB_CIVICA        = 6
ID_TIPO_DOCUMENTO_LIB_ENROLAMIENTO  = 7

ID_RESPONSABILIDAD_IVA_NINGUNO                              =  0
ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO  	            =  1
ID_RESPONSABILIDAD_IVA_NO_RESPONSABLE   		  	            =  3
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA                       =  4
ID_RESPONSABILIDAD_IVA_CONSUMIDOR_FINAL   	  	            =  5
ID_RESPONSABILIDAD_IVA_EXENTO   						  	            =  6
ID_RESPONSABILIDAD_IVA_NO_CATEGORIZADO			  	            =  7
ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA_SOCIAL   	            =  8
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL   	  	      =  9
ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL_SOCIAL   	    = 10
ID_RESPONSABILIDAD_IVA_MONOTRIBUTO_INDEPENDIENTE_PROMOVIDO  = 11

ID_MODIFICADOR_AGREGAR_ITEM                     = 200
ID_MODIFICADOR_ANULAR_ITEM                      = 201
ID_MODIFICADOR_AGREGAR_ITEM_RETORNO_ENVASES     = 202
ID_MODIFICADOR_ANULAR_ITEM_RETORNO_ENVASES      = 203
ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION        = 204
ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION         = 205
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO           = 206
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO            = 207
ID_MODIFICADOR_AGREGAR_ITEM_ANTICIPO            = 208
ID_MODIFICADOR_ANULAR_ITEM_ANTICIPO             = 209
ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO_ANTICIPO  = 210
ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO_ANTICIPO   = 211
ID_MODIFICADOR_DESCUENTO                        = 400
ID_MODIFICADOR_AJUSTE                           = 401
ID_MODIFICADOR_AJUSTE_NEGATIVO                  = 402
ID_MODIFICADOR_AUDITORIA_DETALLADA              = 500
ID_MODIFICADOR_AUDITORIA_RESUMIDA               = 501

ID_MODIFICADOR_AGREGAR                          = ID_MODIFICADOR_AGREGAR_ITEM
ID_MODIFICADOR_ANULAR                           = ID_MODIFICADOR_ANULAR_ITEM

ID_TASA_IVA_NINGUNO = 0
ID_TASA_IVA_EXENTO  = 1
ID_TASA_IVA_10_50   = 4
ID_TASA_IVA_21_00   = 5
ID_TASA_IVA_27_00   = 6

ID_IMPUESTO_NINGUNO = 0
ID_IMPUESTO_INTERNO_FIJO = 1
ID_IMPUESTO_INTERNO_PORCENTUAL = 2

ID_CODIGO_INTERNO = 1
ID_CODIGO_MATRIX  = 2

AFIP_CODIGO_UNIDAD_MEDIDA_SIN_DESCRIPCION            =  0 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO                  =  1 
AFIP_CODIGO_UNIDAD_MEDIDA_METROS                     =  2 
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUADRADO             =  3 
AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUBICO               =  4 
AFIP_CODIGO_UNIDAD_MEDIDA_LITROS                     =  5 
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD                     =  7 
AFIP_CODIGO_UNIDAD_MEDIDA_PAR                        =  8 
AFIP_CODIGO_UNIDAD_MEDIDA_DOCENA                     =  9 
AFIP_CODIGO_UNIDAD_MEDIDA_QUILATE                    = 10 
AFIP_CODIGO_UNIDAD_MEDIDA_MILLAR                     = 11 
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_ANTIB     = 12 
AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD_INT_ACT_INMUNG      = 13 
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO                      = 14 
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO                  = 15 
AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO_CUBICO           = 16 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO                  = 17 
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOLITRO                 = 18 
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_UNIDAD_INT_ACT_INMUNG = 19 
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO                 = 20 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_ACTIVO           = 21 
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_ACTIVO               = 22 
AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_BASE                 = 23 
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTHOR                   = 24 
AFIP_CODIGO_UNIDAD_MEDIDA_JGO_PQT_MAZO_NAIPES        = 25 
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTHOR                  = 26 
AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO_CUBICO          = 27 
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTANT                   = 28 
AFIP_CODIGO_UNIDAD_MEDIDA_TONELADA                   = 29 
AFIP_CODIGO_UNIDAD_MEDIDA_DECAMETRO_CUBICO           = 30 
AFIP_CODIGO_UNIDAD_MEDIDA_HECTOMETRO_CUBICO          = 31 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO_CUBICO           = 32 
AFIP_CODIGO_UNIDAD_MEDIDA_MICROGRAMO                 = 33 
AFIP_CODIGO_UNIDAD_MEDIDA_NANOGRAMO                  = 34 
AFIP_CODIGO_UNIDAD_MEDIDA_PICOGRAMO                  = 35 
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTANT                  = 36 
AFIP_CODIGO_UNIDAD_MEDIDA_UIACTIG                    = 37 
AFIP_CODIGO_UNIDAD_MEDIDA_MILIGRAMO                  = 41 
AFIP_CODIGO_UNIDAD_MEDIDA_MILILITRO                  = 47 
AFIP_CODIGO_UNIDAD_MEDIDA_CURIE                      = 48 
AFIP_CODIGO_UNIDAD_MEDIDA_MILICURIE                  = 49 
AFIP_CODIGO_UNIDAD_MEDIDA_MICROCURIE                 = 50 
AFIP_CODIGO_UNIDAD_MEDIDA_U_INTER_ACT_HORMONAL       = 51 
AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_HORMONAL  = 52 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BASE             = 53 
AFIP_CODIGO_UNIDAD_MEDIDA_GRUESA                     = 54 
AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTIG                   = 55 
AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BRUTO            = 61 
AFIP_CODIGO_UNIDAD_MEDIDA_PACK                       = 62 
AFIP_CODIGO_UNIDAD_MEDIDA_HORMA                      = 63 

AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_NACIONALES                 =    1
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_PROVINCIAL                 =    2
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_MUNICIPAL                   =    3
AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_INTERNOS                    =    4
AFIP_CODIGO_OTROS_TRIBUTOS_INGRESOS_BRUTOS                      =    5
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA                    =    6
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS        =    7
AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_POR_IMPUESTOS_MUNICIPALES =    8
AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES                   =    9
AFIP_CODIGO_OTROS_TRIBUTOS_OTROS                                =   99

AFIP_CODIGO_FORMA_DE_PAGO_CARTA_DE_CREDITO_DOCUMENTARIO       =    1
AFIP_CODIGO_FORMA_DE_PAGO_CARTAS_DE_CREDITO_SIMPLE            =    2
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUE                              =    3
AFIP_CODIGO_FORMA_DE_PAGO_CHEQUES_CANCELATORIOS               =    4
AFIP_CODIGO_FORMA_DE_PAGO_CREDITO_DOCUMENTARIO                =    5
AFIP_CODIGO_FORMA_DE_PAGO_CUENTA_CORRIENTE                    =    6
AFIP_CODIGO_FORMA_DE_PAGO_DEPOSITO                            =    7
AFIP_CODIGO_FORMA_DE_PAGO_EFECTIVO                            =    8
AFIP_CODIGO_FORMA_DE_PAGO_ENDOSO_DE_CHEQUE                    =    9
AFIP_CODIGO_FORMA_DE_PAGO_FACTURA_DE_CREDITO                  =   10
AFIP_CODIGO_FORMA_DE_PAGO_GARANTIAS_BANCARIAS                 =   11
AFIP_CODIGO_FORMA_DE_PAGO_GIROS                               =   12
AFIP_CODIGO_FORMA_DE_PAGO_LETRAS_DE_CAMBIO                    =   13
AFIP_CODIGO_FORMA_DE_PAGO_MEDIOS_DE_PAGO_DE_COMERCIO_EXTERIOR =   14
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_DOCUMENTARIA          =   15
AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_SIMPLE                =   16
AFIP_CODIGO_FORMA_DE_PAGO_PAGO_CONTRA_REEMBOLSO               =   17
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_DOCUMENTARIA                 =   18
AFIP_CODIGO_FORMA_DE_PAGO_REMESA_SIMPLE                       =   19
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO                  =   20
AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_DEBITO                   =   21
AFIP_CODIGO_FORMA_DE_PAGO_TICKET                              =   22
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA              =   23
AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_NO_BANCARIA           =   24
AFIP_CODIGO_FORMA_DE_PAGO_OTROS_MEDIOS_DE_PAGO                =   99





# -----------------------------------------------------------------------------
# Function: dll_version()
# -----------------------------------------------------------------------------
def dll_version():

  #title 
  print "*** DLL VERSION ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # get dll version
  str_version_max_len = 100
  str_version = create_string_buffer( b'\000' * str_version_max_len )
  int_major = c_int()
  int_minor = c_int()
  error = Handle_HL.ConsultarVersionDll( str_version, str_version_max_len, byref(int_major), byref(int_minor) )
  print "DllVersion            : ",
  print error
  print "String Dll Version    : ",
  print str_version.value
  print "Major Dll Version     : ",
  print int_major.value
  print "Minor Dll Version     : ",
  print int_minor.value


# -----------------------------------------------------------------------------
# Function: equipment_machine_version()
# -----------------------------------------------------------------------------
def equipment_machine_version():
  #title 
  print "*** EQUIPMENT MACHINE VERSION ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect                 : ",
  print error

  # get dll version
  str_version_max_len = 100
  str_version = create_string_buffer( b'\000' * str_version_max_len )
  int_major = c_int()
  int_minor = c_int()
  error = Handle_HL.ConsultarVersionEquipo( str_version, str_version_max_len, byref(int_major), byref(int_minor) )
  print "Machinne Version        : ",
  print error
  print "String Machinne Version : ",
  print str_version.value
  print "Major Machinne Version  : ",
  print int_major.value
  print "Minor Machine Version   : ",
  print int_minor.value
  
  # status
  error = Handle_HL.ConsultarEstadoDeConexion()
  print "Conexion Status         : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect               : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header_trailer()
# -----------------------------------------------------------------------------
def set_and_get_header_trailer():

  #title 
  print "*** HEADER & TRAILER ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error


  # set header #1
  error = Handle_HL.EstablecerEncabezado( 1, "Nuevo Encabezado #1" )
  print "Config Header Error   : ",
  print error

  # get header #1
  str_header1_max_len = 100
  str_header1 = create_string_buffer( b'\000' * str_header1_max_len )
  error = Handle_HL.ConsultarEncabezado( 1, str_header1, str_header1_max_len )
  print "Get Header Error      : ",
  print error
  print "Header #1 String      : ",
  print str_header1.value


  # set trailer #1
  error = Handle_HL.EstablecerCola( 1, "Nueva Cola #1" )
  print "Config Trailer Error  : ",
  print error

  # get trailer #1
  str_trailer1_max_len = 100
  str_trailer1 = create_string_buffer( b'\000' * str_trailer1_max_len )
  error = Handle_HL.ConsultarCola( 1, str_trailer1, str_trailer1_max_len )
  print "Get Trailer Error     : ",
  print error
  print "Trailer #1 String     : ",
  print str_trailer1.value


  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header()
# -----------------------------------------------------------------------------
def set_and_get_datetime():
  #title 
  print "*** DATE & TIME ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # get datetime
  str_datetime_max_len = 100
  str_datetime = create_string_buffer( b'\000' * str_datetime_max_len )
  error = Handle_HL.ConsultarFechaHora( str_datetime, str_datetime_max_len )
  print "Get Date & Time Error : ",
  print error
  print "Date & Time           : ",
  print str_datetime.value

  # set datetime (use the same value)
  error = Handle_HL.EstablecerFechaHora( str_datetime.value  )
  print "Set Date & Time Error : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: set_and_get_header()
# -----------------------------------------------------------------------------
def cancel_all():

  #title 
  print "*** CANCEL ALL ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, str_doc_number_max_len )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, str_doc_type_max_len )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # get last error
  error = Handle_HL.ConsultarUltimoError()
  print "Last Error            : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: print_X_and_Z()
# -----------------------------------------------------------------------------
def print_X_and_Z():

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error
  
  # print X
  error = Handle_HL.ImprimirCierreX()
  print "Closure Cashier       : ",
  print error

  # print Z
  error = Handle_HL.ImprimirCierreZ()
  print "Closure Day           : ",
  print error

  # close port
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket
# -----------------------------------------------------------------------------
def ticket():

  #title 
  print "*** TICKET ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUET )
  print "Open                  : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, str_doc_number_max_len )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, str_doc_type_max_len )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error
  
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1.1234", "100.1234", ID_TASA_IVA_21_00, ID_IMPUESTO_INTERNO_FIJO, "7.1234", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.1", 0, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.03", 0, "CodigoInterno4567891123456789012345678901234567891"  )
  print "Uplift                : ",
  print error

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_from_ticket_invoice
# -----------------------------------------------------------------------------
def ticket_from_ticket_invoice():

  #title 
  print "*** TICKET FROM INVOICE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()

  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # open - without customer data previously loaded
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, str_doc_number_max_len )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, str_doc_type_max_len )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1", ".12", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # item 2
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Banana (item2)", "10", "132.087", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno5555588999922255999999600000000000001", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 2                : ",
  print error
  
  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value
  
  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.00", 0, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.00", 0, "CodigoInterno4567890122222222222225678901234567892"  )
  print "Uplift                : ",
  print error

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_invoice
# -----------------------------------------------------------------------------
def ticket_invoice():

  #title 
  print "*** TICKET INVOICE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_invoice_B
# -----------------------------------------------------------------------------
def ticket_invoice_B():

  #title 
  print "*** TICKET INVOICE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_FACTURA )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_debit_note
# -----------------------------------------------------------------------------
def ticket_debit_note():

  #title 
  print "*** TICKET DEBIT NOTE ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error

# -----------------------------------------------------------------------------
# Function: ticket_debit_note_B
# -----------------------------------------------------------------------------
def ticket_debit_note_B():

  #title 
  print "*** TICKET DEBIT NOTE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_credit_note
# -----------------------------------------------------------------------------
def ticket_credit_note():

  #title 
  print "*** TICKET CREDIT NOTE ***"
  
  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "081-0005-0007777" )
  print "main source voucher   : ",
  print error
  
  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: ticket_credit_note_B
# -----------------------------------------------------------------------------
def ticket_credit_note_B():

  #title 
  print "*** TICKET CREDIT NOTE 'B' ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel
  error = Handle_HL.Cancelar()
  print "Cancel                : ",
  print error

  # load customer data
  error = Handle_HL.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3", ID_TIPO_DOCUMENTO_CUIT, "24272242549", ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA )
  print "Customer Data         : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "081-0005-0007777" )
  print "main source voucher   : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "083-00001-00000027" )
  print "Customer Remit #1     : ",
  print error

  # load customer data
  error = Handle_HL.CargarComprobanteAsociado( "082-00003-01003020" )
  print "Customer Remit #2     : ",
  print error

  # open
  error = Handle_HL.AbrirComprobante( ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO )
  print "Open                  : ",
  print error

  # fixed info
  send_fixed_invoice_body( Handle_HL )

  # close
  error = Handle_HL.CerrarComprobante()
  print "Close                 : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: download
# -----------------------------------------------------------------------------
def download():

  #title 
  print "*** DOWNLOAD CTD, CTD A and SUMMARY OF TOTALS ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel vouchers
  error = Handle_HL.Cancelar()
  print "Cancel voucher        : ",
  print error

  # download 
  error = Handle_HL.Descargar( "1", "1", "donwloads" )
  print "Download              : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: audit
# -----------------------------------------------------------------------------
def audit():

  #title 
  print "*** AUDIT ***"

  # get handle from DLL
  Handle_HL = windll.LoadLibrary("EpsonFiscalInterface.dll")

  # connect
  Handle_HL.ConfigurarVelocidad( 9600 )
  Handle_HL.ConfigurarPuerto( "0" )
  error = Handle_HL.Conectar()
  print "Connect               : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel voucher        : ",
  print error

  # audit 
  error = Handle_HL.ImprimirAuditoria( ID_MODIFICADOR_AUDITORIA_DETALLADA, "1", "2" )
  print "Audit Detailed        : ",
  print error

  # try cancel all
  error = Handle_HL.Cancelar()
  print "Cancel Audit          : ",
  print error

  # audit 
  error = Handle_HL.ImprimirAuditoria( ID_MODIFICADOR_AUDITORIA_RESUMIDA, "1", "2" )
  print "Audit Summary         : ",
  print error

  # disconect
  error = Handle_HL.Desconectar()
  print "Disconect             : ",
  print error


# -----------------------------------------------------------------------------
# Function: send_fixed_invoice_body
# -----------------------------------------------------------------------------
def send_fixed_invoice_body( Handle_HL ):

  # get document number
  str_doc_number_max_len = 20
  str_doc_number = create_string_buffer( b'\000' * str_doc_number_max_len )
  error = Handle_HL.ConsultarNumeroComprobanteActual( str_doc_number, str_doc_number_max_len )
  print "Get Doc. Number Error : ",
  print error
  print "Doc Number            : ",
  print str_doc_number.value

  # get document type
  str_doc_type_max_len = 20
  str_doc_type = create_string_buffer( b'\000' * str_doc_type_max_len )
  error = Handle_HL.ConsultarTipoComprobanteActual( str_doc_type, str_doc_type_max_len )
  print "Get Type Doc. Error   : ",
  print error
  print "Doc Type              : ",
  print str_doc_type.value

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3    : ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4    : ",
  print error

  # item  1  - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Sardinas", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item                  : ",
  print error

  # load extra text descripcion  - annulation 
  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #1"  )
  print "Extra Descript. #1 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #2"  )
  print "Extra Descript. #2 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #3"  )
  print "Extra Descript. #3 (A): ",
  print error

  error = Handle_HL.CargarTextoExtra( "Descrip. Extra #4"  )
  print "Extra Descript. #4 (A): ",
  print error

  # item  1  - annulation
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_ANULAR, "Sardinas", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno4567890123456789012345678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 1 - Annulation   : ",
  print error

  # load extra text descripcion
  error = Handle_HL.CargarTextoExtra( "Rodondos (item2)"  )
  print "Extra Descript. #1    : ",
  print error

  # item  2
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Tomates (item2)", "1.0000", "100.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno9999999999999999999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 2                : ",
  print error

  # item  3 - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION, "Cerveza (item3)", "2.0000", "3.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno8228888999922229999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_LITROS )
  print "Item 3 - new          : ",
  print error

  # item  3 - annulation
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION, "Cerveza (item3)", "2.0000", "3.0000", ID_TASA_IVA_21_00, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno8228888999922229999999678901234567890", "", AFIP_CODIGO_UNIDAD_MEDIDA_LITROS )
  print "Item 3 - Annulation   : ",
  print error

  # item  4 - new
  error = Handle_HL.ImprimirItem( ID_MODIFICADOR_AGREGAR, "Banana (item4)", "1.0000", "2.3000", ID_TASA_IVA_10_50, ID_IMPUESTO_NINGUNO, "", ID_CODIGO_INTERNO, "CodigoInterno5555588999922255999999600000000000001", "", AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO )
  print "Item 4 - new          : ",
  print error

  # subtotal
  error = Handle_HL.ImprimirSubtotal()
  print "Subtotal              : ",
  print error

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalBrutoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Gross    : ",
  print error
  print "Subtotal Gross Amount : ",
  print str_subtotal.value

  # get subtotal gross amount
  str_subtotal_max_len = 20
  str_subtotal = create_string_buffer( b'\000' * str_subtotal_max_len )
  error = Handle_HL.ConsultarSubTotalNetoComprobanteActual( str_subtotal, str_subtotal_max_len )
  print "Get Subtotal Net      : ",
  print error
  print "Subtotal Net Amount   : ",
  print str_subtotal.value

  # global discount
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.00", 0, "CodigoInterno4567890123456789012345678901234567890"  )
  print "Discount              : ",
  print error

  # global uplift
  error = Handle_HL.CargarAjuste( ID_MODIFICADOR_AJUSTE, "Recargo global", "90.00", 0, "CodigoInterno4567222222222229012222222201234567890"  )
  print "Uplift                : ",
  print error

  # other taxes 1
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA, "Percepcion por Tasa de IVA", "10.00", ID_TASA_IVA_21_00 )
  print "VAT perception        : ",
  print error

  # other taxes 2
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES, "Otra Percepcion", "5.00", ID_TASA_IVA_NINGUNO )
  print "Other perception      : ",
  print error
  
  # other taxes 3
  error = Handle_HL.CargarOtrosTributos( AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS, "Percepcion de IIBB", "3.00", ID_TASA_IVA_NINGUNO )
  print "Other perception      : ",
  print error

  # payment 1  - new 
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO, 3, "300.00", "Cupones", "Descripcion Pago #1", "VISA -4857, ctas. 3 x $100", "Descripcion Extra #2" )
  print "Payment 1 - new       : ",
  print error

  # payment 1  - annulation
  error = Handle_HL.CargarPago( ID_MODIFICADOR_ANULAR, AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO, 3, "300.00", "Cupones", "Descripcion Pago #1", "VISA -4857, ctas. 3 x $100", "Descripcion Extra #2" )
  print "Payment 1 - annulation: ",
  print error

  # payment 2  - new
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA, 0, "45.00", "Cupones", "Descripcion Pago ii", "CBU -878941494- Pago #2", "Descripcion Extra #2" )
  print "Payment 2 - new       : ",
  print error

  # payment 3  - new
  error = Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA, 0, "25.00", "", "Descripcion Pago iii", "", "" )
  print "Payment 3 - new       : ",
  print error


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
print " "
print " "
print "----Basic Test"
dll_version()
equipment_machine_version()
set_and_get_header_trailer()
set_and_get_datetime()
cancel_all()
print " "
print " "
print "----Testing Sales"
ticket()
ticket_from_ticket_invoice()
ticket_invoice()
ticket_invoice_B()
ticket_debit_note()
ticket_debit_note_B()
ticket_credit_note()
ticket_credit_note_B()
print " "
print " "
print "----Test Close Day"
print_X_and_Z()
audit()
download()





