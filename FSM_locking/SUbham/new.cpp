#include<bits/stdc++.h>

using namespace std;

unordered_map<string , vector<string> > outputToInput;
unordered_map<string , vector<string> > inputToOutput;
unordered_set<string> state_flipflop;
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
unordered_map<string, string> currToNext;
vector<string> nextStates;
vector<string> currentStates;
unordered_set<string> registerList;



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

/*
    Function for finding the DFS of a given node.
*/
void DFS(string currNode , unordered_map<string,bool> &visitedNode)
{
    if(visitedNode[currNode])
        return;
    visitedNode[currNode] = true;
    unordered_map<string , vector<string> >::iterator inputToOutputItr;
    int i;
    inputToOutputItr = inputToOutput.find(currNode);
    if(inputToOutputItr != inputToOutput.end())
    {
        for(i=0;i<inputToOutputItr->second.size();i++)
        {
            cout<<outputToRegister[inputToOutputItr->second[i]]<<" -> "<<inputToOutputItr->second[i]<<"\n";
            cout<<outputToRegister[inputToOutputItr->second[i]]<<" -> "<<currNode<<"\n";
            DFS(inputToOutputItr->second[i] , visitedNode);
        }
    }
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
            if(op.substr(0,2) == "df")
            {
                registerToOutput[gate].push_back(output_operands[i]);
            }
            
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
            registerList.insert(gate);
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



/*
    Check cycles in the circuit (feedbacks in DFFs)
*/
void checkCycle(string startNode, string registerName, string registerInput, unordered_map<string,bool> &visitedNode)
{
    if(startNode == registerInput)
    {
        state_flipflop.insert(registerName);
        //cout<<registerName<<" "<<registerInput<<"\n";
        return;
    }
    unordered_map<string, vector<string> >::iterator inputToOutputItr;
    if(visitedNode[startNode])
        return;
    visitedNode[startNode] = true;
    inputToOutputItr = inputToOutput.find(startNode);
    if(inputToOutputItr != inputToOutput.end())
    {
        for(int i=0;i<inputToOutputItr->second.size();i++)
        {
            checkCycle(inputToOutputItr->second[i], registerName, registerInput, visitedNode);
        }
    }
}
/*
    Initiate check cycle for every register
*/
void initiateCheckCycle()
{
    unordered_map<string,bool> visitedNode;
    unordered_set<string>::iterator nodeItr;
    
    unordered_map<string,vector<string>>::iterator registerToOutputItr;
    for(registerToOutputItr=registerToOutput.begin();registerToOutputItr!=registerToOutput.end();registerToOutputItr++)
    {
        // cout<<registerToInputItr->first<<" "<<registerToInputItr->second<<"\n";
        for(nodeItr = nodes.begin();nodeItr != nodes.end();nodeItr++)
        {
            visitedNode[*nodeItr] = false;
        }
        for(int i = 0; i < registerToOutputItr->second.size(); i++){
            unordered_map<string, vector<string> >::iterator inputToOutputItr;
            inputToOutputItr = inputToOutput.find(registerToOutputItr->second[i]);
            visitedNode[registerToOutputItr->second[i]] = true;
            if(inputToOutputItr != inputToOutput.end())
            {
                for(int j=0;j<inputToOutputItr->second.size();j++)
                {
                    checkCycle(inputToOutputItr->second[j], registerToOutputItr->first,registerToOutputItr->second[i], visitedNode);
                }
            }
        }
    }

}

void find_next_to_curr(string curr){
    unordered_map<string,vector<string>>::iterator registerToOutputItr;
    registerToOutputItr = registerToOutput.find(curr);
    for(int i = 0; i < registerToOutputItr->second.size(); i++){
        string output = registerToOutputItr->second[i];
        for(auto it : registerToInput){
            if(output == it.second){
                currToNext.insert({curr, it.first});
            }
        }
    }
}
void initiate_find_next_to_curr(){
    for(auto it : state_flipflop){
        find_next_to_curr(it);
    }
}


void print(){
    // cout<<" -----------------outputToInput----------------";
    // cout<<endl;
    // for(auto it : outputToInput){
    //     cout<<it.first<<" : ";
    //     for(auto jt : it.second){
    //         cout<<jt<<"  ";
    //     }
    //     cout<<endl;
    // }

    // cout<<" -----------------inputToOutput----------------";
    // cout<<endl;
    // for(auto it : inputToOutput){
    //     cout<<it.first<<" : ";
    //     for(auto jt : it.second){
    //         cout<<jt<<"  ";
    //     }
    //     cout<<endl;
    // }

    // cout<<" -----------------regOutputType----------------";
    // cout<<endl;
    // for(auto it : regOutputType){
    //     cout<<it.first<<" : "<<it.second;
    //     cout<<endl;
    // }

    // cout<<" -----------------operatorOperand----------------";
    // cout<<endl;
    // for(auto it : operatorOperand){
    //     cout<<it.first<<" : ";
    //     for(auto jt : it.second){
    //         cout<<jt<<"  ";
    //     }
    //     cout<<endl;
    // }

    // cout<<" -----------------variableComputed----------------";
    // cout<<endl;
    // for(auto it : variableComputed){
    //     cout<<it.first<<" : "<<it.second;
        
    // }
    // cout<<endl;

    // cout<<" -----------------pathDetails----------------";
    // cout<<endl;
    // for(auto it : pathDetails){
    //     cout<<it<<" ";
        
    // }
    // cout<<endl;

    // cout<<" -----------------nodes----------------";
    // cout<<endl;
    // for(auto it : nodes){
    //     cout<<it<<" ";
        
    // }
    // cout<<endl;

    // cout<<" -----------------registerToInput----------------";
    // cout<<endl;
    // for(auto it : registerToInput){
    //     cout<<it.first<<" : "<<it.second;
    //     cout<<endl;
        
    // }
    // cout<<endl;
    // cout<<" -----------------outputToRegister----------------";
    // cout<<endl;
    // for(auto it : outputToRegister){
    //     cout<<it.first<<" : "<<it.second;
    //     cout<<endl;
        
    // }
    // cout<<" -----------------registerToOutput----------------";
    // cout<<endl;
    // for(auto it : registerToOutput){
    //     cout<<it.first<<" : ";
    //     for(auto jt : it.second){
    //         cout<<jt<<"  ";
    //     }
    //     cout<<endl;
    // }

    // cout<<" -----------------nextStates----------------";
    // cout<<endl;
    // for(auto it : nextStates){
    //     cout<<it<<" ";
    // }
    // cout<<endl;

    // cout<<" -----------------currentStates----------------";
    // cout<<endl;
    // for(auto it : currentStates){
    //     cout<<it<<" ";
    // }
    // cout<<endl;

    // cout<<" -----------------registerList----------------";
    // cout<<endl;
    // for(auto it : registerList){
    //     cout<<it<<" ";
    // }
    cout<<endl;
    cout<<" -----------------next to curr----------------";
    cout<<endl;
    for(auto it : currToNext){
        cout<<it.first<<" "<<it.second<<endl;
    }

}
int main(int agrc , char** argv)
{
    filename = argv[1];
    constructGraph();
    initiateCheckCycle();
    initiate_find_next_to_curr();
    unordered_map<string,vector<string>>::iterator registerToOutputItr;
    registerToOutputItr = registerToOutput.begin();
    cout<<registerToOutputItr->first<<"  "<<registerToOutputItr->second[0];
    
    cout<<endl;
    cout<<"----------------------state flip flop----------------------";
    for(auto it : state_flipflop){
        cout<<it<<endl;
    }
    print();
    return 0;
}