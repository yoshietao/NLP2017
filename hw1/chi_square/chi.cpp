#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <map>


using namespace std;

void setobj(vector<string>& );

int main(int argc,char** argv)
{	
	ifstream data("../polarity_no_1.txt");//argv[1]);
	map <string,vector<int> > count;
	vector<string> obj;
	setobj(obj);
	//cout<<obj[6];
	string get,temp,w1,w2="000";
	int countt = 0, label;
	while(getline(data,get))
	{
		stringstream ss;
		ss<<get;
		ss>>label;
		while(ss>>temp)
		{	countt++;
			w1 = w2;
			w2 = temp;
			//words[temp] = true;
			if (!count[w2].empty())
				count[w2][0]++;
			else
			{
				count[w2].resize(15);
				count[w2][0]++;
			}
			for(int i=0;i<obj.size();i++)
			{
				if (w1 == obj[i])
					count[w2][i+1]++;
			}
			count[w2][14] = label;
		}
	}
	
	cout<<"# of vocabulary"<<countt<<endl;
	////////////////////test//////////////////////
	//for(int i=0;i<count["交通"].size();i++)
	//	cout<<count["太差"][i]<<endl;
	//cout<<count["服务"][0]<<endl;
	
	ofstream ofs("count_chi_no.txt");
	//ofs<<"word "<<"count "<<"服务 "<<"态度 "<<"人员 "<<"环境 "<<"客房 "<<"设备 "<<"空调 "<<"价格 "<<"房价 "<<"交通 "<<"地理 "<<"餐厅 "<<"早餐 "<<"tag"<<endl;
	map<string,vector<int> >::iterator it;
	for(it = count.begin() ; it != count.end() ; it++)
	{
		if(true)//accumulate(it->second.begin(), it->second.end(), 0) > it->second[0]+10 && it->second[0] >=10)
		{
			ofs<<it->first<<' ';
			for(int j=0;j<count["交通"].size();j++)
				ofs<<it->second[j]<<' ';
			ofs<<endl;
		}		
	}
}

void setobj(vector<string>& obj)
{
	obj.push_back("服务");
	obj.push_back("态度");
	obj.push_back("人员");
	obj.push_back("环境");
	obj.push_back("客房");
	obj.push_back("设备");
	obj.push_back("空调");
	obj.push_back("价格");
	obj.push_back("房价");
	obj.push_back("交通");
	obj.push_back("地理");
	obj.push_back("餐厅");
	obj.push_back("早餐");
}