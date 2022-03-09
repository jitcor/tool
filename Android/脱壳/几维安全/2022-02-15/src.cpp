#include<fstream>
#include<string>


typedef unsigned char	u1;
typedef unsigned int	u4;

struct DexHeader {
	u1  magic[8];
	u4  checksum;
	u1  signature[20];
	u4  fileSize;
	u4  headerSize;
	u4  endianTag;
	u4  linkSize;
	u4  linkOff;
	u4  mapOff;
	u4  stringIdsSize;
	u4  stringIdsOff;
	u4  typeIdsSize;
	u4  typeIdsOff;
	u4  protoIdsSize;
	u4  protoIdsOff;
	u4  fieldIdsSize;
	u4  fieldIdsOff;
	u4  methodIdsSize;
	u4  methodIdsOff;
	u4  classDefsSize;
	u4  classDefsOff;
	u4  dataSize;
	u4  dataOff;
};


struct KiwiDexItem {
	u4 dexSize;
	u4 dexOff;
};

struct KiwiHeader {
	u1 magic[8];
	u4 dexCount;
	u4 dataOff;
	KiwiDexItem items[0];
};

//=====>>>样本<<<=====
//链接：https://pan.baidu.com/s/1h1dUCLixSykuI7KvQAsIrw 
//提取码：it9k
//--来自百度网盘超级会员V4的分享

int main() {
	std::ifstream ifs("classes.dex", std::ifstream::binary);
	ifs.seekg(0, ifs.end);
	auto fileLen = static_cast<int>(ifs.tellg());
	auto rawDexBuf = new u1[fileLen];
	ifs.seekg(0, ifs.beg);
	ifs.read(reinterpret_cast<char *>(rawDexBuf), fileLen);
	ifs.close();

	auto dexHeader = reinterpret_cast<DexHeader*>(rawDexBuf);
	auto kiwiHeader = reinterpret_cast<KiwiHeader*>(rawDexBuf + dexHeader->dataOff + dexHeader->dataSize);
	auto kiwiDexItems = kiwiHeader->items;
	auto dexCount = kiwiHeader->dexCount;
	auto dexBasePtr = reinterpret_cast<u4>(kiwiHeader) + kiwiHeader->dataOff;

	for (size_t dexIndex = 0; dexIndex < dexCount; dexIndex++)
	{
		auto  dexPtr = reinterpret_cast<u1*>(dexBasePtr + kiwiDexItems[dexIndex].dexOff);
		for (size_t i = 0; i < 9; ++i)
		{
			dexPtr[i] ^= dexIndex + i + dexCount + 2;
		}
		std::ofstream ofs("classes_" + std::to_string(dexIndex) + ".dex", std::ofstream::binary);
		ofs.write(reinterpret_cast<char*>(dexPtr), kiwiDexItems[dexIndex].dexSize);
		ofs.close();
	}

	return 0;
}