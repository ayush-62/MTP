#include<bits/stdc++.h>

using namespace std;

unordered_map<string , vector<string> > outputToInput;
unordered_map<string , vector<string> > inputToOutput;
unordered_map<string , char> regOutputType;
unordered_map<string , string > operatorOperand;
unordered_map<string , string > inputOperator;
unordered_map<string , string > operatorName;
unordered_map<string , bool> visited;
unordered_map<string , bool> variableComputed;
unordered_set<string> pathDetails;
unordered_set<string> nodes;
unordered_map<string,string>  registerToInput  ;
unordered_map<string,string> outputToRegister;
unordered_map<string,vector<string> > registerToOutput;
vector<string> nextStates;
vector<string> currentStates;
vector<string> registerList;
vector<string> state_flipflop;


unordered_map<string,int> pathCount;
string filename;

vector<string> tokenizer(string str, char delimiter)
{
    stringstream ss(str);
    string word;
    vector<string> arr;
    while(!ss.eof())
    {
        getline(ss, word, delimiter);
        arr.push_back(word);
    }
    return arr;
}

int DFS(string start, string currNode ,unordered_map<string , vector<string> > graph, unordered_map<string,bool> &visitedNode)
{
    
    if(visitedNode[currNode])
        {
            // if(currNode == start) return 1;
            // else return 0;
            return 1;
        }
    visitedNode[currNode] = true;
    unordered_map<string , vector<string> >::iterator Itr;
    int i;
    Itr = graph.find(currNode);
    int rv = 0;
    if(Itr != outputToInput.end())
    {
        for(i=0;i<Itr->second.size();i++)
        {
            // cout<<Itr->second[i]<<" ";
            rv = max(rv, DFS(start, Itr->second[i] , graph ,visitedNode));
        }
    }
    return rv;
}

void constructGraph()
{
    ifstream fin;
    string line, gate, input, output, op;
    char operandType;
    vector<string> tokens, input_operands, output_operands; 
    int position,i,j;
    fin.open(filename);
    while(getline(fin,line))
    {
        tokens.clear();
        input_operands.clear();
        output_operands.clear();
        tokens = tokenizer(line, ' ');
        if(tokens.size() >= 2)
        {
            op = tokens[0];
            gate = tokens[1];
            //registers.insert()
            //cout<<gate<<"[ shape = \"rectangle\"]\n";
        }
        for(int i=3;i<tokens.size()-1;i++)
        {
            position = 0;
            while(tokens[i][position++] != '(');
            input = "";
            operandType = tokens[i][position-2];
            while(tokens[i][position]!=')')
            {
                input+=tokens[i][position++];
            }
            regOutputType[input] = operandType;
            if(operandType == 'Y' || operandType == 'Q' || operandType == 'X' || operandType == 'N')
            {
                regOutputType[input] = operandType;
                output_operands.push_back(input);
            }
            else
                input_operands.push_back(input);
        }
        for(int i=0;i<input_operands.size();i++)
        {
            //cout<<input_operands[i]<<" -> "<<gate<<";\n";
            nodes.insert(input_operands[i]);
        }
        for(int i=0;i<output_operands.size();i++)
        { 
            nodes.insert(output_operands[i]);
            registerToOutput[gate].push_back(output_operands[i]);
            //cout<<gate<<" -> "<<output_operands[i]<<";\n";
        }

        //updating the adjacency list
        for(i=0;i<output_operands.size();i++)
        {
            for(j=0;j<input_operands.size();j++)
            {
                outputToInput[output_operands[i]].push_back(input_operands[j]);
            }

        }
        for(i=0;i<input_operands.size();i++)
        {
            for(j=0;j<output_operands.size();j++)
            {
                inputToOutput[input_operands[i]].push_back(output_operands[j]);
            }
        }

        //get the pair for register names and it's input
        if(op.substr(0,2) == "df")
        {
            registerToInput[gate] = input_operands[0];
            registerList.push_back(gate);
        }
        for(i=0;i<input_operands.size();i++)
        {
            if(input_operands[i] == "rst" || op.substr(0,2) != "df" || input_operands[i] == "clk") 
                continue;
            // registerToInput[gate] = input_operands[i];
        }
        for(i=0;i<output_operands.size();i++)
        {
            operatorOperand[output_operands[i]] =  op;
            operatorName[output_operands[i]] = gate;
            //if(op.substr(0,2) != "df")
                //continue;
            outputToRegister[output_operands[i]] = gate;
        }
    }
}

void find_state_flipflop(){
    visited.clear();
    for(auto it : registerToInput){
        if(DFS(it.second, it.second, outputToInput, visited ) == 1){
            state_flipflop.push_back(it.second);
        }
    }
}

int main(int agrc , char** argv)
{
    filename = argv[1];
    constructGraph();
    // DFS("_______1652","_______1652", outputToInput ,visited);
    find_state_flipflop();
    for(auto it : state_flipflop){
        cout<<it<<endl;
    }
    return 0;
}