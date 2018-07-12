import binascii, cv2
import numpy as np
h = 'ffd8ffdb00430010081010100810101010101010102020202010102040202020204040404040404040404080404040404040404080404080808080804040808080808080808080ffdb00430110101020102040202040804040408080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080ffc000110801e0028003012200021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475767778797a838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae1e2e3e4e5e6e7e8e9eaf1f2f3f4f5f6f7f8f9faffc4001f0100030101010101010101010000000000000102030405060708090a0bffc400b51100020102040403040705040400010277000102031104052131061241510761711322328108144291a1b1c109233352f0156272d10a162434e125f11718191a262728292a35363738393a434445464748494a535455565758595a636465666768696a737475767778797a82838485868788898a92939495969798999aa2a3a4a5a6a7a8a9aab2b3b4b5b6b7b8b9bac2c3c4c5c6c7c8c9cad2d3d4d5d6d7d8d9dae2e3e4e5e6e7e8e9eaf2f3f4f5f6f7f8f9faffda000c03010002110311003f00e671460fa1ad2fb38fee83f8506dfd8d6f731b1998f71462b44db8f4fc690c07d3f3a1c87ca50c5255ff00b3fb506dff000a570e52851571a0fa7e268f229dc2c53a2ad982830351cc162a5255a301cf514860345c2c56a2acf907d28f20ff00fae8e60b15a8ab3e41f4c5279268e60b15e92acf92690c07d314730ac4149563c93e8690c27de8b8ec40692a6f28ff00f5e8f29bb7eb4730ac43454a636ee3f2a4f2cfad170b1152d49e5b7a527967d47e345c2c4668a90c6d479668b8588e92a428de8690a1f7fc68b8ec328a71534bb0fb53b80ca434fd87d282a7d295c5619453b6b7a5054fa1a771d86d253c29a369a2e2b0dc514ec1cd183e868b80da5a5c518345c62528a307d297145c42514518a2e014b4518a2e21451482968b80a296905140c5a28a05002d1494b408296928a005a2928340052e6928a005a29052d030e28145068b80514506810945140a7718b49451484145145300a5a41451700a514868a6c0534525152074fb14f63f851e58ff00f5d3c506b0b9a11ec149b054868a2e3b1198c7b527962a6a4345c643b07a0a3ca53daa5a70145c457f257d28f247a7e55628a2e3b15fc914df27d87e26ad0a3145c562a98451e48ab58a4c517195c40293c81e86ad628a2e162b7d9f340b71eb566969f30ac54f20521b71e82ae1a4c52b858a46df9a436fed57c0a08a3982c67fd9fda8f207b55ec52d0e571d8cf36fec693ecff4ad1c52628b858cef23da90dbe7b0ad1a4c53e6158cefb3fb521b65f4fceb488a314ae3b1986dfd00a4fb37a8cd6a6da4db4ee2b199f671d90521b63e82b508a42a29730ec659b7f6a4fb37b56a151e94051e945c2c657d9bda8fb30f4fcab5828f4a368cd3b858c9fb28fafd68fb281d88ad8083d29760f4a2e2b18a6dbdbf4a6fd9fd0e2b69905208d68e60b18ff66fa521b6fa56cf962831ad1cc3b18bf663d8d1f673dff4ad9f297d29444be828e6158c5fb37d68fb3d6d18d68f2d4f6a7cc16317ecf47d98d6d794be94a225fa51cc1630fecf47d9bdab6cc43d68f2568e60b1882dcfafe74bf673e8315b6211eb418568e60b189e41ec3f1a4f20d6df923ffd5479028e60b18bf673e94180f715b7e40c5218053e60b189e41f4a3c93ff00ebadaf23e9408051cd7158c5f20fd690c2de86b73c8f6148d6f473058c4f24d1e49adaf23d38a3c8a39876313c93ef49e51adcf207a534c03d314390ad7317c96f6fc68f28ff00faab67ecf47d9feb47307298be49f7a3ca3ef5b66dfdbf3a436fed473058c531103fc693cb3ea3f0ad936fed4df23da9f3058c7f2cd2ec35ade452f91ed4730ac646c3e949b0fa56bf93ec28f207a7e54ee16323cb3d851b0fb66b5fc91d38a0c1ed4730ac6418dbd28286b58c1c742693ecff00ecd1cc162e6f140905657da3dff3a04fc7de1f9d4f2957354b8f5a5de2b2c4fe8734a27f7a5ca1734f78f5146e1eb599e7fbd1f68f7028e50b9a9ba8de3d6b2fed1ee3f0a513fb8a5619a7be8dd59be7d1e7fbd160348352ee159a273ebf9d3bcff7a560344352ee159be7ff00b4297cff007a2c068e69370aa027fc7e94bf68f7a760b97811413547cfa5f3e95865dc8a504550f3e944e33d4516117f34a2a8f9e28f3c7afeb45865d38a4c8aa867f7a6f9fef9a2c05c2692aa79c3d68330f5a2c05b0452e4553f3a944c28b016ce28e2aaf9c3d693ce14ac05be2835544c3de9de70f5a76027a4a87cd1ea28f347ad20263462a1130f5a5f307ad16025a5150f983b51e60f5a009c1a5aafe68cf5a70905160263462a2120f5a5f307ad160b92521a8cc8293cc1eb4012d385422414a241eb4012d2547e60f5147983d68024a51516f1ea28de3d45004b4a2a2de29438a009452d45bc7ad2ef14012500547bc7ad3838f5a009283d2981a9430a005c528a4dc29370a063e90d30b8a378a0438d2520607b8a5c8a005c518a28c8a003147d28269a4f3400ec52d2034714008450452d191400d207a0a36d3a83400c22803da9c6814c426290a8a7d25031bb051b47a53b3466811c8e4fbd149456e677173ef464fa9a4a281dc0d2ee34940a0571771f5a5dc7fbc69b49458771fb8fa9a031a6d25160b8fdedeb46e6f5fca9b4868b05c7ef6f534091bd4fe34c349de9582e49e637a51e6b7b9a8cf5a29582e49e737ae28f39ea2a28e541cc4c266ef9fc297ce6f7fc6a1ef494583989fcf34be79f7aaf494582e58f3cfbfe1479e6abd250e23b967cf6f53479e7d4fe355a8a3942e59139ff00f5d28b83e95568a7ca172dfda4d1f68f723eb5528a5ca172d8b8f714efb47bfe5548d19a3942e5dfb47bd02e4fb7e754b3450a2172ff00da3e9f852fda3dc56752d0e217347ed1ef8a3ed1ee7f3acda38a5ca3b9a46e71dcd28b91eb59838a33e94f94573545cffb54bf68ac9cfa9a507eb4b9477357ed1ef49e7fbfe559793eb464fa9a390398d51703d7f3a5fb47fb5595b8d018e7ad1ca1cc6b7da3dcd2fda3dcd64ee3ebf9d1b8fad2e40e635c5c0f5a3ed1591b9bfbd4a19bd68e50e635bed14e13fbd646e6ee45018d1ca1cc6c09fde9c271eb58dbdbd6943b51ca173644feff00ad384f58bbcf7e697cc6a1c4773684dee29de7d62095a97cd6a3942e6d79e7dbf3a4338cf5ac6f39bebf4a04cfeff8d1ca17367cf1eb409fdeb1fce6f71f4a3cd6f52697285cda5987ad3d671584266a709dbd7f3a7ca17373cf1ea297cfac41707dcd1f68fad1ca1736bce1ea051e70f5ac5fb4376cd2fda0ff00fae8e50b9b4251eb4a265f506b145c7bd2fda3d48a5ca17367cef43479dee3f3ac6171ef8f6147da3dff003a3942e6cf9a3b914a261f5fa5630b8ff2297ed1f5a2c06cf9a3bd2f982b1d6e3de8fb4fb9fc28b05cd7328ff2693cdac9fb40fef527da067ab1fc28b05cd7f3051e60f5ac913f3d4d067ff6a8e515ccf028c55cf27e9f852187d01ad2f626c54a3156fc9fff00551e47b5170b15293156cc3f5148613ee68b858ab455af278a4f24fa1a3982c56a2ac7927d293c93ef45c2c414953f927de8311c5170b10521a9fca3ef47947d28b858828153188fbfe149e51f7a2e1621228a9fcb3ef49e59f4a570b115254de59a464a2e2b115254bb0d1e59a2e3b115254de59a4f2da9dc2c45454a6334dd868b8588e969fb0e68d868b8586514fd8690a1f4a2e161a68a76d3e8451b4d3b858652d2eda369f434ae036929c41f434983e9f9d1701075a334b8a4c1a0560a297068c503684a514629450014518a314c42528a3140a062d145140094a28c5028b80528a290d021451451400a29690502818b45028a0414b4868a00296928a005a29296800a28a4a005a28a2800a5a4a0d0014525145862d2834940a057168a4a33405c5cfbd04d251400bf89a2928a00e8cc43d29be4d5ac5380ac2e6a54f27d7f414be4fd6ad814a00a2e2b144c3eb9a4f27eb57980a4228e61d8a5e4d1e4f3d2ae814628b858a261a4f27f0abf8a6914ee1628793ef4861e7bfe15788a5c52b858a1e4fb0fc68f26afedcd2e0517033fc81479157f028c0a3982c67f93ed48601fddfc6b4703d28da3d28b858cd30fb52183dab4f6d215145c2c66791ed4791ec6b4b60a028ed45c2c67791ed4860f615a61052ec145c2c651807a0a69b719e833ed5adb05218c5170b191e473f768f279edf8d6a98c7a0a3cb1ec28b858ca300f40693c8f6ad5f2c7b51e58f4a2e064983ebf852183d88ad6f287a5279628b8193e451e456b7943bd1e50f6a3982c64180fb52791f4ad83151e55170b18de41f6fca8301fff00556c793ed4861fa1a7cc1631cc07d29041ed5b061a3c9a3982c63f907d3347907d2b63caa3c9f6a2e1631fc93e94791ed5b061f6a430fb51cc1631fc93e949e49f4fcab5fcaf6a3c9f6cd1cc16323c93fdda5f28fa56b793ec68f268e60b191e47f934be41ed8ad7f268f27da9f30ac63984fa6693ca3ed5b0611e949e48f4a3982c63f95f5a0c47d0fe35b061a6f93ec68e70b193e51f7a0c7f5ad6f2693c9e7b51cc16327cb3e946c3e95abe47b51e4fb51cc2e532b61a4287d2b54c34860f634738f94cb0868d87bd6a793ed9a3c8f6a7cc2e532f61f4a369cf4ad3309f4a4f20fa0a3982c66953df8a4da6b4c41ed4e1053e60e532f69f4a369f435a7e40f414183d851cc0e265e0fa51835a5e41ff00f5527939ec7f1a398394ceda690835a3e473de8f23eb4f985633f1460d68791ec4d27934b98394a183462af791f5a5107b555c5ca50c1a3157fc8a4f20e7a0a3982c50c1a31578c07d291a1fa7e228e60b1d05028a5ac0d05cd06928a00334bda9281400ea4a28a000d34d3a90d031869452d1400868ed4b498a0043d6814b8a5c5201a052d18a5c50002834a28a6025371cd3a8a004a0d06928016969b46680061494668140086929c69290051494b4005385369c3f5a005a0502973400845068a4269805029b4e534805a00a28a0031486968a00691ef40145385002628c53a8a603714a0514b40098146052d14009814981e829d450034a8f4a028f4a752d003360a4d82a4a28023d8293cb152d2d004263147962a62290d0042631ed49e50a9a968022110a5110a97b528345c088c43b8a4f2854f4868b8880c5ed4862fa558ef49c517195fcafa51e5558a28115cc549e57b559a0d1702b18bda8117b54f4a29dc0afe50f4fce97c91e9fad5914b8a3981a29987fc8a6f93f53f5aba4518a3982c2628229d41a00677a294f5a4a40028a0d140c28a4a075a0070a0d1486800a00a28140062940a28a00290d14500252d145000296933450006928a5a004a434ea3148061148453cd21a6036945140a40068c52d1400da4a7521a004a72d20a70a005a434b450034d0453b145003314a053a8a004a2968a00290d2d06980cc528a5a2900504d0690f5a003346692968016969052d001494b49400a2969296980514bda8140062968145000690d2d21a0000a5c50296801b4829c690d002834b4d14b4001a4a751400ded40a5a2800a434b41a006d14b8a2801452d20fe74b40828a514b400d141a0514c043d29a3ad2b520eb4807518a334500368c53a802801b453a80281898a29d486810d345068a06028ef45140051de9334a2800c514b486800a314a28340094b4945002d21a5141a006514ea43400da296929000a075a28c5002d2d252d002d06928a005a4a28a005a4a28a0028a5a4a005a4a334500068a2909a00534d141349400b476a051de80014ea414b4c028a28a0028a28a00052d1486801734a29b4a28014d1de8c52d20014b482834001a4a514530014a2929450014529a4a004a28345002d14869680128a5a2801b4b4b45020a514948680145068a2801a7ad029694500250294d266800a052679a5a062d2d20a2800348694d20a0043494e34d34008690d29a4a4014a292945002d14a292980a3ad068ef4520128a43d696980a2969052d2010d34d39a9a68010d14525002f41453734b400b4a2905028017bd1451400514b453013bd14514805a4345140094506928014d276a3b521a004ef4b4518a06029475a314b408514b4829680128a5a280128a5a2800a4a5a280129cb494a0d301d45028a0043494eef4948029681450014b4868a60141a290d0019a2928a4029a0521a05301c294520a5140062929d48680129294d2520169293ad14c42d04d2134da063c9c8a4c5277a514080d385140a000514b41a0634d0294d2500148697bd06801b453a96900cc52e2969334c04345068a40028a2928014d1499a2980e5a514d14a0d2014d34d38d34d301a6929c690520100a5028a5140098a294d140051451400514521a005a28a2800a281450018a4a752500252538d36800a5a281400b451450316971494a2810628a2968001484734b477a006d253e9a6980945145201c29d4c14b9a005a2814530168a4a5a000d028a28003494b45201b4529a2980946296814000a70a4a70a002834a690d0034d18a5ef49400c1477a502968012929d462801a29d40a280168a4a2801696928a004340a29680128a0d25002d2d3682680149a434941a402514528a601486948a4a00281452e29000a051450029a4a28a004349de9c690d300a2928a4029a2814500277a29692800a28345001452d1400528a4a51400b486969a680034d34a7a525030a51d692945002d2d0281d6800a05068a0419a334945003a94d3696800a28a0d031314502968105068349400b45251400e145252d0028a290528a005a4a5a2980d34869c69a69005028c528a6028a51499a33400ea43499a0d001494518a00052d028a040690d2d21a06145028a002929d450020a5a28ef48028a5a298080518a5a2801a69ad4fa4c50034514ec514806d14ec525000692969280014a2929450006834b4d34001a4a0d250029a43413484d0014a29a29c280168a4a514005253a8a006d28a5a2800a434b450025028a281851487ad2d0021a28a2801075a5a052d0014b48296800341a283400da5a28a00052d02968109450692801d4a290528a000d369f46280194b4b8a2818945140a04029c2905385001451da834c06f7a294d02900514514c0434529a4340099a5ed48681480514a2901a5a004ed4a29a29c29801e9494b46280128a28a0028a09a6d003a8a4a2900a29734d349400ecd19a6d19a007e68148296980b452506800a434668a401494b484e4d0025028345002d06928a004a4a7521a0069a4ef4e34da0614a0d2502801d452669075a0078a5a6d3a810514a290d00141eb4514009452d140c6d06968a004a0d149400528a4c53850002969052d002d068a280128a0d250028a0d2668a04068a292801c29c29b4a2801d4520a28016928a4a00281499a3bd003a9453452d003850690514c04a5a09a4a402d14da0d301c4d14d14b4001a4341a2800a33494b4802941a60a514c0793499a4a2800a28a2800a29692800a4a5a4ef4800d253a8c500252e2814e1400828ef4b45301290d2d21a402668a290d002f7a5a4140a0051d6834b4530128a5a2900948694d21a0069a69a71a69eb40c28a28a002945028c50028a5a0502810b4528a43400514506800a294521a06145145002514a69bde8017b52d251400b452529a000529a4a28010d2529a4340051451408296814b40094a28a2818ea4a4a2810b48694521a0614514b9a0029452528a005141a28a0425141a69a005341a6d02801734668a280034945068016945252ad00368a2969806281452d0006814521a00514b480d28a401494b450020eb4b4514000eb451450014502968010d253a8a6037b50696929009452d068180a7536973408283d6928cd00069a69692818869b4f34da042502968a06029d48296800a5a4a5a00296928a0028a290d002d14945002d14945002d2506928016814528a40252d141a60149450680128a28a00314a292945021c28a4a2818b494506800a28a4a005a29296800a2929680014a293bd2d0028a0d25140843494a692818528a414a2810514a0514009452d18a002945029450030514514c051d683451400869294d250028a7534528a4038514828a005a4a28140051452d00145251400b494506801693bd19a2800a2968a062628a5a4a0043494a692800a28a0502034869690d03128a5a4a00514b48296800141a4cd068003452506900a6928a2800a28a2818514514082968a29800a51451400b4868a43400506928a0028a4a51400528a414b400b45145001452528a0028c52d068012834ea4c734009452d14000a3bd14b400941a292800349450680014b4945021d4b4d14b9a00297b52034b400a29452528a008e9451da8a6014941a2800a074a3bd2ad200ef4a28a280128cd29a6d0014b4def4a2801d45252d000690529a414001a0d1494000a51494b400b4b49499a005a43484d140c4a283450019a3348690d021d9a29a696818b45145020a0d148690c28a28a60140a052d2010d2d145300a4a5a2800145145200a5c5145300a297349400868a0d25200a28349400b451da9450014b40a5a6025141a4a005140a28a0075149477a042d0683486800a33494503168a4cd28a04069294d140c434d34e34940094b46281400a28a0d005021694520a05002d28a4349400514945300a28a0f5a002945029450014514734800d21a5a4a004a2968a00051451400b486928a005a0d028cd030a28a2810869294d21a06149451da800a296928101a4a5a2818940eb451400b45251400b49452d000296814b40082968141a000d14525200a28a2800a5a292980519a4cd25003a96999a5a005a28a434001a28a4a402d28a414b4c051452519a00534941a6e6900e06814da5a603a826928a005cd266928a005cd1486814085a5a4a70a0028a052d002629294d0281852529a3b500145141a62168ef48296900521a53494009466928a6029a05251400a29c29bde945003a8a4a5a402514a692800a4a5a2801a68a3bd140077a5a4ef45001450692818b451450025068a0f4a004a28a0d020a4a534940052d20a5a061451450021a2968a004c528a28a005a514d14b400a3ad068a4a0029294d349a402d2d36968016909a28a6021a4a0d250316969b40a043b34514500149de83450014a09a4a0d002e69474a6d14001a0d1da8a40029d4d14e14c05a28a5a006d2d06928014d2514bde8100a5145140c5a5a4a2810b494b494000a0d21a4cd002d26690d02801734b9a68a5cd003a8cd369680128a294530128a5a280014b4502900e14520345300a4a5a3bd20128a3bd068012968a0d30128ef4528a40252529a4a005a4a5a4a602d25069290c0d252d140843494e34940c05140a5a005a2928a042d21a33466818868345277a005ed4a0d141a005a434525000693bd29a4a000528a4a51400b41a0514008690d38d34d00028a292900a294d252d002514b494c03bd21a51d28a002814a052d0021a4a7521a000528a4a51400a2834506800a4a42697340051452679a0078a29a296810a2969334668014d1499a28181a4a28a042514514000a5a052d002514bde8a002940e2968a602014b8a5a434001a43413494805145148680149a4345140c5145028cd0216928cd19a602514514800d068a280128a534d34001a0d1450014514500141a5a280105028a2800a28ef41a06277a28a29005149cd2d30014a28a2800a434b48680034868a050014a2929680168a28a40069283d690d300341a4a290c29452528a042f7a28a2800a00a5a2980014b45140052529a28010d2529a2801074a0d0692801690d2d250014528a5a00414ea4a0f5a0414525266801d4b4dcd28a005a28a5a00292969680128a5ef48698094b4945003c529a4a42680178a29290d00068a3349400b9e68a4a0d20168a414b40051450280034529a4a004a283d68a005cd251450014d34b45300a0d1494805a292945002d145140051452d0034d277a71a4a004a294d21340c4a51450280168a2929005277a5a29801a414a692801681cd14b4800d252d06980da3bd145001451de8a005340a414ea0028a28a005a29296800a5a4a28016929294d00277a4a5a4a003ad145140094b4b4500028a5a281094514bda801a6929d48681882945252ad003a9690528a042f6a0d1453010d068a2900945140a005a4a4a2980b452514805a29334530168a4a2900b4b494a2980518a29690086834a69b400514514009451450014521a4a005345252d03014a290528a005a28a0502168345068010d2529a4a0043451de8a062d2528a5a004a2968a004a0d2d1400da5a2928014d252d1480414b4521a6006928a2800a5140a5a004a28cd21a000f5a5a6d2d003a814829680168a075a2800a4a5a4a000d252f6a4a005a05252d0014b4945002d029b9a28016969281408290d2d140094a28a2801452d2528a005a2928a000d2507ad14c028a434b400da3348690d002d28a6d2d0028a5a6d2d002d1451480052d276a2980ea2928ed400b452502800a4a5a434001eb487ad2d34d200a28a280014b40a28181a05252d003851482968105068a0d002521a5a69340c0d029296801475a75301a703400b45028a0028a2928003494b49400a28a28a0029294d21a0029296814000a5a4a28010d141eb476a004a5a4a2801697b520eb4b400a296928a005a434506800a4ef4506801296928a007668a68a5a005a4a28a0028a4a5140051477a2801681486968016969a334b4085349494b4005252d25300a514945003474a2968c71400da514b8a50280129452e28a402521e94b450020eb4504d25002d28a69a05003a8a28a60141a5a28010d369c4d21a4313bd068a050216928a3b5030a052528a0070a29b4a298871a4a4cd148029bde968a0621a5a4a280169474a6d3874a00514b482945000692968a0069a28349400b4b9a6d0280168ed4525002d21a0d1400514506800a4a28a0028a2945001da9690f4a28017bd14949de801d40a4cd1400b4945140051494b4001a5a414e02801314014b4500277a5c5145002628fd29693bd0014b49450014a29b40a0075029a29734c43a928a2800349de968340082968c52d020a28a5a0621a0d1494001a43487ad277a005a4a53d293bd0014b494b400b4b4d14b9a402d1499a5cd0025069690d30128a5a43486252d20a5a04252d1450014a29b4b400a6928cd266818a6928a2800a28a05002d38520a5a005a0514b4009452d06801a69ad4fa69a006d2d21a5a0028345140051451da800a3345140094529a43400514528a00075a5a4a4a0028a28a00281486945002d14525002d28a414b400b8a05145020a5a4a5a002900a0d140051451de800a439a5a4340c4a2968a04250281d697bd300a281466900b452514c05a05028a0429a2928a0614868a43400525149400b45252d002d25145001de969281d6801c28a4a5a400296939a2800340a28a0028a53453013bd21a53494804a28a28181a28a2810520a0d140c293b0245369450048b452034b4085a514da5a0028a4268cd0029a69a5a43d6818945145001451450014a2928a00297b521a2800a4a5a4a0028a28a005a4345140052514b4009452d140051451400a2969a2945002d2e79a4141a005a09a6e6826810b9e28cd3696818b9a0536968017bd1de929681052d028a004a5a0514c029294d20a4007a5141a280168a0514c4141a0d25031290d3e9b4009494a6834804a75369453016928345001452d148614a29294f4a04141a4a2800a5a4a2801d41a4068cd00148694d14008692834b400941a5a4a062521a534500252d277a2801c29475a6d1400f14a4d3051400a4f340a4a2801c6928a4a042d04d3734503168a4a5a002945251400b9a43452668014d2514500145145002d1451400528a0514009452d14084a29452d031b4b4b41e94084345141a062514b49400514502801696814940829452528a00514668345300ef4945140051494a29001a4a2834c05a283499a043a8a4a01a0629a69a5a4c50025069dda8c50036814b8a5028012968c529a004a28a05002f6a69a75349a004a28a28ffa28a4a005a5a4a2800a28a29000a5a28a60149de94d21a060690d148690051da8a2800a05251400ea334d34bde8016834946680168a4a0f5a0414941a4a063a80690528a062d2d145020a28a0d0021a39a28a004ef4bde90528a005145145002d0281d683400514514c03bd2d252e2900503a502969884a434ea46a006d14b487a5002d1494b400a3a52d252d002514a6928014d252d21a0028a0d25002d25145002d1da8a31401fffd9'

h = binascii.a2b_hex(h)
print binascii.a2b_hex(h.encode('hex'))
while True:
    i = cv2.imdecode(np.fromstring(h, dtype=np.uint8),1)
    cv2.imshow('i',i)
    if cv2.waitKey(30) & 0xFF == ord('q'):
            break
# data = binascii.a2b_hex(h)
# with open('image.jpg', 'wb') as image_file:
#     image_file.write(data)
