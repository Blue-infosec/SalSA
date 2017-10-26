"""
check sction names for common packers/uncommon names
"""

# list of common packer section names
packers = {
  '.aspack': 'Aspack packer',
  '.adata': 'Aspack packer/Armadillo packer',
  'ASPack': 'Aspack packer',
  '.ASPack': 'ASPAck Protector',
  '.boom': 'The Boomerang List Builder (config+exe xored with a single byte key 0x77)',
  '.ccg': 'CCG Packer (Chinese Packer)',
  '.charmve': 'Added by the PIN tool',
  'BitArts': 'Crunch 2.0 Packer',
  'DAStub': 'DAStub Dragon Armor protector',
  '!EPack': 'Epack packer',
  'FSG!': 'FSG packer (not a section name, but a good identifier)',
  '.gentee': 'Gentee installer',
  'kkrunchy': 'kkrunchy Packer',
  '.mackt': 'ImpRec-created section',
  '.MaskPE': 'MaskPE Packer',
  'MEW': 'MEW packer',
  '.MPRESS1': 'Mpress Packer',
  '.MPRESS2': 'Mpress Packer',
  '.neolite': 'Neolite Packer',
  '.neolit': 'Neolite Packer',
  '.nsp1': 'NsPack packer',
  '.nsp0': 'NsPack packer',
  '.nsp2': 'NsPack packer',
  'nsp1': 'NsPack packer',
  'nsp0': 'NsPack packer',
  'nsp2': 'NsPack packer',
  '.packed': 'RLPack Packer (first section)',
  'pebundle': 'PEBundle Packer',
  'PEBundle': 'PEBundle Packer',
  'PEC2TO': 'PECompact packer',
  'PECompact2': 'PECompact packer (not a section name, but a good identifier)',
  'PEC2': 'PECompact packer',
  'pec1': 'PECompact packer',
  'pec2': 'PECompact packer',
  'PEC2MO': 'PECompact packer',
  'PELOCKnt': 'PELock Protector',
  '.perplex': 'Perplex PE-Protector',
  'PESHiELD': 'PEShield Packer',
  '.petite': 'Petite Packer',
  '.pinclie': 'Added by the PIN tool',
  'ProCrypt': 'ProCrypt Packer',
  '.RLPack': 'RLPack Packer (second section)',
  '.rmnet': 'Ramnit virus marker',
  'RCryptor': 'RPCrypt Packer',
  '.RPCrypt': 'RPCrypt Packer',
  '.seau': 'SeauSFX Packer',
  '.sforce3': 'StarForce Protection',
  '.spack': 'Simple Pack (by bagie)',
  '.svkp': 'SVKP packer',
  'Themida': 'Themida Packer',
  '.Themida': 'Themida Packer',
  '.taz': 'Some version os PESpin',
  '.tsuarch': 'TSULoader',
  '.tsustub': 'TSULoader',
  '.packed': 'Unknown Packer',
  'PEPACK!!': 'Pepack',
  '.Upack': 'Upack packer',
  '.ByDwing': 'Upack Packer',
  'UPX0': 'UPX packer',
  'UPX1': 'UPX packer',
  'UPX2': 'UPX packer',
  'UPX!': 'UPX packer',
  '.UPX0': 'UPX Packer',
  '.UPX1': 'UPX Packer',
  '.UPX2': 'UPX Packer',
  '.vmp0': 'VMProtect packer',
  '.vmp1': 'VMProtect packer',
  '.vmp2': 'VMProtect packer',
  'VProtect': 'Vprotect Packer',
  '.winapi': 'Added by API Override tool',
  'WinLicen': 'WinLicense (Themida) Protector',
  '_winzip_': 'WinZip Self-Extractor',
  '.WWPACK': 'WWPACK Packer',
  '.yP': 'Y0da Protector',
  '.y0da': 'Y0da Protector',
}


# list of common section names
common = {
  '.00cfg': 'Control Flow Guard (CFG) section (added by newer versions of Visual Studio)',
  '.arch': 'Alpha-architecture section',
  '.autoload_text': 'cygwin/gcc; the Cygwin DLL uses a section to avoid copying certain data on fork.',
  '.bindat': 'Binary data (also used by one of the downware installers based on LUA)',
  '.bootdat': 'section that can be found inside Visual Studio files; contains palette entries',
  '.bss': 'Uninitialized Data Section',
  '.BSS': 'Uninitialized Data Section',
  '.buildid': 'gcc/cygwin; Contains debug information (if overlaps with debug directory)',
  '.CLR_UEF': '.CLR Unhandled Exception Handler section',
  '.code': 'Code Section',
  '.cormeta': '.CLR Metadata Section',
  '.complua': 'Binary data, most likely compiled LUA (also used by one of the downware installers based on LUA)',
  '.CRT': 'Initialized Data Section (C RunTime)',
  '.cygwin_dll_common': 'cygwin section containing flags representing Cygwin capabilities',
  '.data': 'Data Section',
  '.DATA': 'Data Section',
  '.data1': 'Data Section',
  '.data2': 'Data Section',
  '.data3': 'Data Section',
  '.debug': 'Debug info Section',
  '.debug$F': 'Debug info Section (Visual C++ version <7.0)',
  '.debug$P': 'Debug info Section (Visual C++ debug information: precompiled information',
  '.debug$S': 'Debug info Section (Visual C++ debug information: symbolic information)',
  '.debug$T': 'Debug info Section (Visual C++ debug information: type information)',
  '.drectve ': 'directive section (temporary, linker removes it after processing it; should not appear in a final PE image)',
  '.didat': 'Delay Import Section',
  '.didata': 'Delay Import Section',
  '.edata': 'Export Data Section',
  '.eh_fram': 'gcc/cygwin; Exception Handler Frame section',
  '.export': 'Alternative Export Data Section',
  '.fasm': 'FASM flat Section',
  '.flat': 'FASM flat Section',
  '.gfids': 'section added by new Visual Studio (14.0); purpose unknown',
  '.giats': 'section added by new Visual Studio (14.0); purpose unknown',
  '.gljmp': 'section added by new Visual Studio (14.0); purpose unknown',
  '.glue_7t': 'ARMv7 core glue functions (thumb mode)',
  '.glue_7': 'ARMv7 core glue functions (32-bit ARM mode)',
  '.idata': 'Initialized Data Section (Borland Compiler)',
  '.idlsym': 'IDL Attributes (registered SEH)',
  '.impdata': 'Alternative Import data section',
  '.itext': 'Code Section (Borland Compiler)',
  '.ndata': 'Nullsoft Installer section',
  '.orpc': 'Code section inside rpcrt4.dll',
  '.pdata': 'Exception Handling Functions Section (PDATA records)',
  '.rdata': 'Read-only initialized Data Section (Microsoft and Borland Compiler)',
  '.reloc': 'Relocations Section',
  '.rodata': 'Read-only Data Section',
  '.rsrc': 'Resource section',
  '.sbss': 'GP-relative Uninitialized Data Section',
  '.script': 'Section containing script',
  '.shared': 'Shared section',
  '.sdata': 'GP-relative Initialized Data Section',
  '.srdata': 'GP-relative Read-only Data Section',
  '.stab': 'Created by Haskell compiler (GHC)',
  '.stabstr': 'Created by Haskell compiler (GHC)',
  '.sxdata': 'Registered Exception Handlers Section',
  '.text': 'Code Section',
  '.text0': 'Alternative Code Section',
  '.text1': 'Alternative Code Section',
  '.text2': 'Alternative Code Section',
  '.text3': 'Alternative Code Section',
  '.textbss': 'Section used by incremental linking',
  '.tls': 'Thread Local Storage Section',
  '.tls$': 'Thread Local Storage Section',
  '.udata': 'Uninitialized Data Section',
  '.vsdata': 'GP-relative Initialized Data',
  '.xdata': 'Exception Information Section',
  '.wixburn': 'Wix section',
  'BSS': 'Uninitialized Data Section (Borland Compiler)',
  'CODE': 'Code Section (Borland Compiler)',
  'DATA': 'Data Section (Borland Compiler)',
  'DGROUP': 'Legacy data group section',
  'edata': 'Export Data Section',
  'idata': 'Initialized Data Section (C RunTime)',
  'INIT': 'INIT section (drivers)',
  'minATL': 'Section that can be found inside some ARM PE files; purpose unknown',
  'PAGE': 'PAGE section (drivers)',
  'rdata': 'Read-only Data Section',
  'sdata': 'Initialized Data Section',
  'shared': 'Shared section',
  'Shared': 'Shared section',
  'testdata': 'section containing test data (can be found inside Visual Studio files)',
  'text': 'Alternative Code Section',
}


SECTION_ALERT = """
Application Section Names:
{0}"""

KNOWN_COMMON = """
  Known common section names (can indicate functionality):
{0}
"""

KNOWN_BAD = """
  Known bad section names:
{0}
"""

UNKNOWN = """
  Unknown section names (can indicate an unknown packer):
{0}
"""


def run(peobject):
  alerts = []
  unknown = []
  known_bad = []
  known_common = []
  # loop through each section
  for s in peobject.dict()['SECTIONS']:
    # check for known/unknown sections
    if (s['Name'] in packers):
      known_bad.append('\t\t' + s['Name'] + ' : ' + packers[s['Name']])
    elif (s['Name'] in common):
      known_common.append('\t\t' + s['Name'] + ' : ' + common[s['Name']])
    else:
      unknown.append('\t\t' + s['Name'] + ' : ???')
  # parse each section
  alert = ''
  if known_common:
    alert += KNOWN_COMMON.format('\n'.join(known_common))
  if known_bad:
    alert += KNOWN_BAD.format('\n'.join(known_bad))
  if unknown:
    alert += UNKNOWN.format('\n'.join(unknown))
  # generate final alert
  if alert:
    alerts.append(SECTION_ALERT.format(alert))
  return alerts
