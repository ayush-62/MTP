#include<bits/stdc++.h>

using namespace std;

//global values

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


unordered_map<string,int> pathCount;

// for adjacency list of the partial graph
unordered_map<string , vector<string> > stateGraph;
unordered_map<string , vector<string> > reverseStateGraph;
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

unordered_set<string> cycleRegistersList;

/*
    Check cycles in the circuit (feedbacks in DFFs)
*/
void checkCycle(string startNode, string registerName, string registerInput, unordered_map<string,bool> &visitedNode)
{
    if(startNode == registerInput)
    {
        cycleRegistersList.insert(registerName);
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
    
    unordered_map<string,string>::iterator registerToInputItr;
    for(registerToInputItr=registerToInput.begin();registerToInputItr!=registerToInput.end();registerToInputItr++)
    {
        // cout<<registerToInputItr->first<<" "<<registerToInputItr->second<<"\n";
        for(nodeItr = nodes.begin();nodeItr != nodes.end();nodeItr++)
        {
            visitedNode[*nodeItr] = false;
        }
        unordered_map<string, vector<string> >::iterator inputToOutputItr;
        inputToOutputItr = inputToOutput.find(registerToInputItr->second);
        visitedNode[registerToInputItr->second] = true;
        if(inputToOutputItr != inputToOutput.end())
        {
            for(int i=0;i<inputToOutputItr->second.size();i++)
            {
                checkCycle(inputToOutputItr->second[i], registerToInputItr->first, registerToInputItr->second, visitedNode);
            }
        }
        //break;
    }

}

/*
    Verilog to bench
*/

void verilogToBench()
{
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    for(outputToInputItr = outputToInput.begin() ; outputToInputItr != outputToInput.end() ; outputToInputItr++)
    {
        //DFF outputs Q and Q_n
        if(regOutputType[outputToInputItr->first] == 'N')
            cout<<outputToInputItr->first<<" = "<<operatorOperand[outputToInputItr->first]<<"n(";
        else
            cout<<outputToInputItr->first<<" = "<<operatorOperand[outputToInputItr->first]<<"(";
        for(int i=0;i<outputToInputItr->second.size()-1;i++)
        {
            cout<<outputToInputItr->second[i]<<",";
        }
        cout<<outputToInputItr->second[outputToInputItr->second.size()-1]<<")";
        cout<<"\n";
    }
}

/*
    Print graph based on a starting node
*/
void printGraphNode(string startNode)
{
    if(visited[startNode])
        return;
    visited[startNode] = true;
    unordered_map<string,vector<string> >::iterator inputToOutputItr = inputToOutput.find(startNode);
    if(inputToOutputItr != inputToOutput.end())
    {
        for(int i=0;i<inputToOutputItr->second.size();i++)
        {
            cout<<inputToOutputItr->first<<" -> "<<inputToOutputItr->second[i]<<"\n";
            printGraphNode(inputToOutputItr->second[i]);
        }
    }

}


/*
    Prints a graph 
    Adjacency list as input
*/
void printGraph(unordered_map<string , vector<string> > graph)
{
    unordered_map<string , vector<string> >::iterator graphItr;
    int i;
    for(graphItr=graph.begin() ; graphItr != graph.end() ; graphItr++)
    {
        //cout<<graphItr->first<<" : ";
        for(i=0;i<graphItr->second.size();i++)
        {
            //if(graphItr->first == "clk" || graphItr->first == "rst")
                //continue;
            //cout<<graphItr->first<<" -> "<<graphItr->second[i]<<"\n";
            cout<<graphItr->first<<"->"<<graphItr->second[i]<<"\n";
        }
        //cout<<"\n";
    }

}

/*
    Prints a bench file  
    Adjacency list as input
*/
void printBench(unordered_map<string , vector<string> > graph)
{
    unordered_map<string , vector<string> >::iterator graphItr;
    int i;
    for(graphItr=graph.begin() ; graphItr != graph.end() ; graphItr++)
    {
        if(regOutputType[graphItr->first] == 'N')
            cout<<graphItr->first<<" = "<<operatorOperand[graphItr->first]<<"n (";
        else
            cout<<graphItr->first<<" = "<<operatorOperand[graphItr->first]<<" (";
        for(i=0;i<graphItr->second.size()-1;i++)
        {
            //if(graphItr->first == "clk" || graphItr->first == "rst")
                //continue;
            //cout<<graphItr->first<<" -> "<<graphItr->second[i]<<"\n";
            cout<<graphItr->second[i]<<",";
        }
        cout<<graphItr->second[graphItr->second.size()-1]<<")\n";
    }

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

/*
    Initiate the function for DFS of a given node.
*/
void initiateDFS(string currNode)
{   
    unordered_map<string,bool> visitedNode;
    unordered_set<string>::iterator nodesItr;
    for(nodesItr=nodes.begin();nodesItr!=nodes.end();nodesItr++)
    {
        visitedNode[*nodesItr] = false;
    }
    unordered_map<string , vector<string> >::iterator inputToOutputItr;
    int i;
    inputToOutputItr = inputToOutput.find(currNode);
    if(inputToOutputItr != inputToOutput.end())
    {
        for(i=0;i<inputToOutputItr->second.size();i++)
        {
            cout<<outputToRegister[inputToOutputItr->second[i]]<<" -> "<<inputToOutputItr->second[i]<<"\n";
            cout<<currNode<<" -> "<<outputToRegister[inputToOutputItr->second[i]]<<"\n";
            DFS(inputToOutputItr->second[i] , visitedNode);
        }
    }
}

void getPath(string currNode)
{
    //if(operatorOperand[currNode].substr(0,2) == "df")
      //  cout<<currNode<<" "<<operatorOperand[currNode]<<"\n";
    if(visited[currNode])// || (currNode.substr(0,10) == "next_state" && operatorOperand[currNode].substr(0,2) == "df"))
    {
        return;
    }
    unordered_map<string , vector<string> >::iterator itr = outputToInput.find(currNode);
    if(itr == outputToInput.end())
        return;
    pathDetails.insert(operatorName[currNode] + " [shape=\"rectangle\" ; style = \"filled\" ; color = \"grey\"]\n");
    pathDetails.insert(operatorName[currNode] + " -> " + currNode + "\n");
    visited[currNode] = true;
    //cout<<operatorName[currNode]<<" [shape=\"rectangle\"]\n";
    //cout<<operatorName[currNode]<<" -> "<<currNode<<"\n";
    for(int i=0;i<itr->second.size();i++)
    {
        pathDetails.insert(itr->second[i] + " -> " + operatorName[currNode] + "\n");
        //cout<<itr->second[i]<<" -> "<<operatorName[currNode]<<"\n";
        //cout<<operatorOperand[currNode].substr(0,2)<<" ";
        //
        if(itr->second[i] != "reset" & currNode.substr(0,10) != "next_state" && currNode != "valid") // itr->second[i] != "clk" &&
        {
            stateGraph[itr->second[i]].push_back(currNode);
            reverseStateGraph[currNode].push_back(itr->second[i]);
            variableComputed[itr->second[i]] = false;
            //cout<<itr->second[i]<<" -> "<<currNode<<"\n";
        }

        /* 
            For restricting the further scan at next_state_* 
        */
        if(itr->second[i].substr(0,10) == "next_state" || operatorOperand[currNode].substr(0,2) == "df")
        {
            continue;
        }
        getPath(itr->second[i]);
    }
    //cout<<currNode<<" ";
}


void printPath(string currNode)
{
    unordered_map<string , vector<string> >::iterator itr = inputToOutput.find(currNode);
    if(itr == inputToOutput.end())
        return;
    for(int i=0;i<itr->second.size();i++)
    {
        cout<<currNode<<" -> "<<itr->second[i]<<"\n";
    }
}

void getPathInputToOutput(string currNode)
{
    //cout<<currNode<<" ";
    if(visited[currNode])
    {
        return;
    }
    unordered_map<string , vector<string> >::iterator itr = inputToOutput.find(currNode);
    if(itr == inputToOutput.end())
        return;
    //pathDetails.insert(operatorName[currNode] + " [shape=\"rectangle\" ; style = \"filled\" ; color = \"grey\"]\n");
    //pathDetails.insert(operatorName[currNode] + " -> " + currNode + "\n");

    //cout<<operatorName[currNode]<<" [shape=\"rectangle\"]\n";
    //cout<<currNode<<" -> "<<operatorName[currNode]<<"\n";
    variableComputed[currNode] = false;
    //cout<<currNode<<" ";
    visited[currNode] = true;
    for(int i=0;i<itr->second.size();i++)
    {
        
        pathDetails.insert(itr->second[i] + " -> " + operatorName[currNode] + "\n");
        //cout<<operatorName[currNode]<<" -> "<<itr->second[i]<<"\n";
        //cout<<currNode<<" -> "<<itr->second[i]<<"\n";
        getPathInputToOutput(itr->second[i]);
    }
    //cout<<currNode<<" ";
    //printPath(currNode);
}




void makePath(string currNode , stack<string> &paths)
{
    variableComputed[currNode] = true;

    unordered_map<string,vector<string> >::iterator itr;
    itr = stateGraph.find(currNode);
    if(itr != stateGraph.end()){
        for(int i=0;i<itr->second.size();i++)
        {
            //cout<<itr->second[i]<<" ";
            if(!variableComputed[itr->second[i]])
                makePath(itr->second[i],paths);
        }
    }
    paths.push(currNode);
}


void createOperation(string op , string output , char regOutputType)
{
    //cout<<op<<" ";
    string operation;
    int i;
    if(op.substr(0,3) == "inv")
        cout<<"bool "<<output<<" = !"<<reverseStateGraph.find(output)->second[0]<<";";
    else if(op.substr(0,3) == "dfr" || op.substr(0,3) == "dfx")
    {
        if(regOutputType == 'N')
            cout<<"bool "<<output<<" = !"<<reverseStateGraph.find(output)->second[0]<<";";
        else    
            cout<<"bool "<<output<<" = "<<reverseStateGraph.find(output)->second[0]<<";";
    }
    else if(op.substr(0,3) == "and")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        for(i=0;i<itr->second.size()-1;i++)
        {
            tempOperation += itr->second[i];
            tempOperation += " & ";
        }
        tempOperation += itr->second[itr->second.size()-1];
        cout<<"bool "<<output<<" = "<<tempOperation<<";";
    }
    else if(op.substr(0,2) == "or")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        for(i=0;i<itr->second.size()-1;i++)
        {
            tempOperation += itr->second[i];
            tempOperation += " | ";
        }
        tempOperation += itr->second[itr->second.size()-1];
        cout<<"bool "<<output<<" = "<<tempOperation<<";";
    }
    else if(op.substr(0,4) == "nand")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        for(i=0;i<itr->second.size()-1;i++)
        {
            tempOperation += itr->second[i];
            tempOperation += " & ";
        }
        tempOperation += itr->second[itr->second.size()-1];
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op.substr(0,3) == "nor")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        for(i=0;i<itr->second.size()-1;i++)
        {
            tempOperation += itr->second[i];
            tempOperation += " | ";
        }
        tempOperation += itr->second[itr->second.size()-1];
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "o21ai_0")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "("+itr->second[0] + " | " + itr->second[1] + ") & (" + itr->second[2] + ")";
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "o22ai_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "!("+itr->second[0] + " | " + itr->second[1] + ") | !(" + itr->second[2] + " | " + itr->second[3] + ")";
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "o211ai_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "("+itr->second[0] + " | " + itr->second[1] + ") & (" + itr->second[2] + ") & (" + itr->second[3] + ")";
        cout<<"bool "<<output<<" = !("<<tempOperation<<")";
    }
    else if(op == "o221ai_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "("+itr->second[0] + " | " + itr->second[1] + ") & (" + itr->second[2] + " | " + itr->second[3] + ") & (" + itr->second[4] + ")";
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "o32ai_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "!("+itr->second[0] + " | " + itr->second[1] + " | " + itr->second[2] + " ) | !(" + itr->second[3] + " | " + itr->second[4] + ")";
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "a21oi_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "(" + itr->second[0] + " & " + itr->second[1] + ") | " + itr->second[2]; 
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "a221oi_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "(" + itr->second[0] + " & " + itr->second[1] + ") | (" + itr->second[2] + " & " + itr->second[3] + ") | (" + itr->second[4] + ")"; 
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "a211oi_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "(" + itr->second[0] + " & " + itr->second[1] + ") | (" + itr->second[2] + ") | (" + itr->second[3] + ")"; 
        cout<<"bool "<<output<<" = !("<<tempOperation<<");";
    }
    else if(op == "a222oi_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "!(" + itr->second[0] + " & " + itr->second[1] + ") & !(" + itr->second[2] + " & " + itr->second[3] + ") & !(" + itr->second[4] + " & " + itr->second[5] + ")"; 
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "mux2i_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = itr->second[2] + " ? !" + itr->second[0] + " : !" + itr->second[1];
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "mux2_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = itr->second[2] + " ? " + itr->second[0] + " : " + itr->second[1];
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "xnor2_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "(!" + itr->second[0] + " & !" + itr->second[1] + ") | (" + itr->second[0] + " & " + itr->second[1] + ")";
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
    else if(op == "xor2_1")
    {
        string tempOperation = "";
        unordered_map<string , vector<string> >::iterator itr;
        itr = reverseStateGraph.find(output);
        if(itr == reverseStateGraph.end())
            return;
        tempOperation = "(!" + itr->second[0] + " & " + itr->second[1] + ") | (" + itr->second[0] + " & !" + itr->second[1] + ")";
        cout<<"bool "<<output<<" = ("<<tempOperation<<");";
    }
}

void initiateMakePath()
{
    stack<string> paths;

    
    unordered_map<string,bool>::iterator itr;
    
    for(itr = variableComputed.begin();itr != variableComputed.end() ; itr++)
    {
        if(!itr->second)
        {
            makePath(itr->first , paths);
        }
    }
    while(!paths.empty())
    {
        
        if(reverseStateGraph.find(paths.top()) == reverseStateGraph.end())
        {
            //cout<<paths.top()<<" "<<0<<"\n";
            cout<<"bool "<<paths.top()<<";\n";
        }
        else{
            //cout<<operatorOperand[paths.top()]<<" "<<regOutputType[paths.top()]<<" : ";
            //cout<<paths.top()<<" ";//;<<outputToInput.find(paths.top())->second.size()<<"\n";
            createOperation(operatorOperand[paths.top()] , paths.top() , regOutputType[paths.top()]);
            cout<<"\n";
        }

        paths.pop();
    }
}

/*
    Checks whether the input can reach a register
*/
void tracePath(string startNode,string registerName, unordered_map<string,bool> &visited, unordered_set<string> &registerList, unordered_set<string> &gatesList , unordered_set<string> &intermediateInputList , int &count)
{

    int i,j;
    unordered_map<string,vector<string> >::iterator inputToOutputItr = inputToOutput.find(startNode);
    visited[startNode] = true;
    if(inputToOutputItr != inputToOutput.end())
    {
        for(i=0;i<inputToOutputItr->second.size();i++)
        {
            // cout<<startNode<<" -> "<<inputToOutputItr->second[i]<<"\n";
            if(visited[inputToOutputItr->second[i]])
                continue;
            if(operatorOperand[inputToOutputItr->second[i]].substr(0,2) == "df" && registerName != operatorName[inputToOutputItr->second[i]])
            {
                registerList.insert(operatorName[inputToOutputItr->second[i]]);
                // cout<<startNode<<" -> "<<inputToOutputItr->second[i]<<"\n";
                continue;
            }
            // cout<<registerName<<" : "<<operatorOperand[inputToOutputItr->second[i]]<<"\n";
            gatesList.insert(operatorOperand[inputToOutputItr->second[i]]);
            intermediateInputList.insert(inputToOutputItr->second[i]);
            count++;
            //no require to go further 2. As we require only count == 1 candidates.
            if(count == 2)
                return;
            tracePath(inputToOutputItr->second[i], registerName, visited, registerList, gatesList , intermediateInputList ,  count);
        }
    } 
}

/*
    Find paths between two registers 
*/

unordered_set<string> graph_reg;
unordered_map<string,vector<string> > invOutputToRegisters;
unordered_map<string,int> registerOccuranceCount;
unordered_map<string,vector<pair<string,string> > > registerPair;
void findPaths(string startNode,string registerName)
{
    unordered_map<string,bool> visited;
    unordered_map<string,string> next_state_to_curr_state;
    unordered_set<string> registerList;
    unordered_set<string> gatesList;
    unordered_set<string> intermediateInputList;
    unordered_set<string>::iterator itr;
    int i;
    for(itr=nodes.begin();itr!=nodes.end();itr++)
    {
        visited[*itr] = false;
    }
    int count = 0;
    /*unordered_map<string,vector<string> >::iterator inputToOutputItr = inputToOutput.find(startNode);
    //cout<<node<<" : ";
    visited[startNode] = true;
    cout<<startNode<<":";
    if(inputToOutputItr != inputToOutput.end())
    {
        for(i=0;i<inputToOutputItr->second.size();i++)
        {
            if(visited[inputToOutputItr->second[i]])
                return;
            tracePath(inputToOutputItr->second[i],visited,registerList);
            cout<<"\n";
        }
    }*/
    pathCount.clear();
    tracePath(startNode,registerName, visited , registerList , gatesList , intermediateInputList , count);
    unordered_set<string>::iterator graphItr;
    unordered_set<string>::iterator gatesListItr;
    for(graphItr = registerList.begin();graphItr != registerList.end();graphItr++)
    {
        if(registerName == *graphItr)
        {
            continue;
        }
        // cout<<registerName<<" -> "<<*graphItr<<"\n";
        graph_reg.insert(registerName+" -> "+*graphItr);
        next_state_to_curr_state[registerName] = *graphItr;
        pathCount[registerName]++;
    }
    unordered_map<string,int>::iterator pathCountItr;
    unordered_map<string,vector<string> >::iterator registerToOutputItr;
    unordered_set<string>::iterator intermediateInputListItr;
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    bool isOutputData;
    for(pathCountItr=pathCount.begin();pathCountItr!=pathCount.end();pathCountItr++)
    {
        isOutputData = false;
        if(pathCountItr->second == 1 && count == 1)
        {
            registerToOutputItr = registerToOutput.find(next_state_to_curr_state[pathCountItr->first]);
            if(registerToOutputItr != registerToOutput.end())
            {
                for(int i=0;i<registerToOutputItr->second.size();i++)
                {
                    //cout<<registerToOutput.find(pathCountItr->first)->second[0]<<" "<<regOutputType[registerToOutput.find(pathCountItr->first)->second[0]]<<" ";
                    if(registerToOutputItr->second[i].substr(0,3) == "out" || regOutputType[registerToOutput.find(pathCountItr->first)->second[0]] == 'S' || regOutputType[registerToOutput.find(pathCountItr->first)->second[0]] == '0' || regOutputType[registerToOutput.find(pathCountItr->first)->second[0]] == '1')
                    {
                        isOutputData = true;
                        break;
                    }
                }
            }
            if(!isOutputData)
            {
                string gate;
                for(gatesListItr=gatesList.begin();gatesListItr!=gatesList.end();gatesListItr++)
                {
                    gate = *gatesListItr;
                }
                for(intermediateInputListItr=intermediateInputList.begin();intermediateInputListItr!=intermediateInputList.end();intermediateInputListItr++)
                {
                    //cout<<*intermediateInputListItr<<" ";
                    outputToInputItr = outputToInput.find(*intermediateInputListItr);
                    for(int i=0;i<outputToInputItr->second.size();i++)
                    {
                        //cout<<operatorOperand[outputToInputItr->second[i]]<<" ";
                        if(operatorOperand[outputToInputItr->second[i]].substr(0,3) == "inv")
                        {
                            if(outputToInput.find(outputToInputItr->second[i])->second[0] == "rst" && gate.substr(0,3) == "and")
                            {
                                invOutputToRegisters[outputToInputItr->second[i]].push_back(pathCountItr->first + " -> " + next_state_to_curr_state[pathCountItr->first]);
                                registerOccuranceCount[pathCountItr->first]++;
                                registerOccuranceCount[next_state_to_curr_state[pathCountItr->first]]++;
                                registerPair[outputToInputItr->second[i]].push_back(make_pair(pathCountItr->first , next_state_to_curr_state[pathCountItr->first]));
                                // nextStates.push_back(pathCountItr->first);
                                // currentStates.push_back(next_state_to_curr_state[pathCountItr->first]);
                                //cout<<outputToInputItr->second[i]<<" : "<<pathCountItr->first<<" : "<<pathCountItr->first<<" -> "<<next_state_to_curr_state[pathCountItr->first]<<" "<<count<<"\n";
                            }
                        }
                    }
                }
            } 
        }
    }
}

void initiateFindPath()
{
    unordered_map<string,string>::iterator registerToInputItr;
    unordered_map<string,string>::iterator outputToRegisterItr;
    for(outputToRegisterItr=outputToRegister.begin();outputToRegisterItr!=outputToRegister.end();outputToRegisterItr++)
    {
        //cout<<outputToRegisterItr->first<<" "<<outputToRegisterItr->second<<"\n";
        findPaths(outputToRegisterItr->first,outputToRegisterItr->second);
    }
    // for(registerToInputItr=registerToInput.begin();registerToInputItr!=registerToInput.end();registerToInputItr++)
    // {
    //     //cout<<registerToInputItr->first<<" "<<registerToInputItr->second<<"\n";
    //     //findPaths(registerToInputItr->second,registerToInputItr->first);
    // }
    // unordered_map<string,int>::iterator pathCountItr;
    // for(pathCountItr=pathCount.begin();pathCountItr!=pathCount.end();pathCountItr++)
    // {
    //     if(pathCountItr->second == 1)
    //         cout<<pathCountItr->first<<" "<<pathCountItr->second<<"\n";
    // }
}

void printNextStateToCurrentState(string node , unordered_map<string,bool> &visited)
{
    unordered_map<string,vector<string> >::iterator inputToOutputItr;
    visited[node] = true;
    inputToOutputItr = inputToOutput.find(node);
    if(inputToOutputItr == inputToOutput.end())
        return;
    for(int i=0;i<inputToOutputItr->second.size();i++)
    {
        if(visited[inputToOutputItr->second[i]])
            continue;
        if(operatorOperand[inputToOutputItr->second[i]].substr(0,2) == "df")
        {
            cout<<node<<" -> "<<inputToOutputItr->second[i]<<"\n";
        }
        else
        {
            cout<<node<<" -> "<<inputToOutputItr->second[i]<<"\n";
            printNextStateToCurrentState(inputToOutputItr->second[i], visited);
        }
    }
}

void initiatePrintNextStateToCurrentState(string start)
{
    unordered_map<string,bool> visited;
    int i;
    unordered_set<string>::iterator itr;
    // for(itr=nodes.begin();itr!=nodes.end();itr++)
    // {
    //     visited[*itr] = false;
    // }
    unordered_map<string,vector<string> >::iterator inputToOutputItr;
    inputToOutputItr = inputToOutput.find(start);
    if(inputToOutputItr == inputToOutput.end())
        return;
    for(i=0;i<inputToOutputItr->second.size();i++)
    {
        for(itr=nodes.begin();itr!=nodes.end();itr++)
        {
            visited[*itr] = false;
        }
        printNextStateToCurrentState(inputToOutputItr->second[i] , visited);
    }

}

bool checkStatePresent(string stateNode)
{
    vector<string>::iterator currentStatesItr;
    for(currentStatesItr=currentStates.begin();currentStatesItr!=currentStates.end();currentStatesItr++)
    {
        if(*currentStatesItr == stateNode)
            return true;
    }
    return false;

}

/*
    Check whether a state is present in the given list
*/
bool checkStatePresentInGivenList(vector<string> statesList , string stateNode)
{
    int i;
    for(i=0;i<statesList.size();i++)
    {
        if(statesList[i] == stateNode)
            return true;
    }
    return false;
}

/*
    get the dependent registers upon a selected next state.
*/
void getCurrentStateToNextStateCount(string outputNode , unordered_map<string,bool> &visitedNodes,int &countCurrentStates)
{
    if(visitedNodes[outputNode])
        return;
    visitedNodes[outputNode] = true;
    if(outputToRegister.find(outputNode) != outputToRegister.end() && checkStatePresent(outputToRegister[outputNode]))
    {
        countCurrentStates++;
        cout<<outputToRegister[outputNode]<<"\n";
    }    
    int i;
    unordered_map<string,vector<string> >::iterator outputToInputItr;

    outputToInputItr = outputToInput.find(outputNode);
    if(outputToInputItr != outputToInput.end())
    {
        for(i=0;i<outputToInputItr->second.size();i++)
        {
            getCurrentStateToNextStateCount(outputToInputItr->second[i],visitedNodes,countCurrentStates);
        }
    }

}

/*
    function to initiate the function to get the count of the number of 
    current states depending on a given next state.
*/
void initiateGetCurrentStateToNextStateCount()
{
    vector<string>::iterator nextStatesItr;
    vector<string>::iterator currentStatesItr;
    unordered_set<string>::iterator nodesItr;
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    unordered_map<string,vector<string> >::iterator registerToOutputItr;

    unordered_map<string,bool> visitedNodes;
    int i,j,countCurrentStates;

    

    for(nextStatesItr=nextStates.begin();nextStatesItr!=nextStates.end();nextStatesItr++)
    {
        registerToOutputItr = registerToOutput.find(*nextStatesItr);
        cout<<"Selected next state : "<<*nextStatesItr<<"\n";
        for(nodesItr=nodes.begin();nodesItr!=nodes.end();nodesItr++)
        {
            visitedNodes[*nodesItr] = false;
        }
        countCurrentStates = 0;
        cout<<"List of current states the next state "<<*nextStatesItr<<" is dependent on :\n";
        if(registerToOutputItr != registerToOutput.end())
        {
            for(i=0;i<registerToOutputItr->second.size();i++)
            {
                outputToInputItr = outputToInput.find(registerToOutputItr->second[i]);
                //cout<<outputToInputItr->first<<" : ";
                if(outputToInputItr != outputToInput.end())
                {
                    for(j=0;j<outputToInputItr->second.size();j++)
                    {
                        getCurrentStateToNextStateCount(outputToInputItr->second[j],visitedNodes,countCurrentStates);
                    }
                }
            }
        }
        cout<<"Count of current states : "<<countCurrentStates<<"\n";
    }
}


/*
    count the number of intermediate registers dependent
*/
void countIntermediateRegisters(string startNode , unordered_map<string,bool> &visitedNodes , unordered_set<string> &intermediateRegisters , unordered_set<string> &allIntermediateRegisters)
{
    if(visitedNodes[startNode])
        return;
    visitedNodes[startNode] = true;
    if(outputToRegister[startNode].substr(0,11) != "_next_state" && operatorOperand[startNode].substr(0,2) == "df")
    {
        intermediateRegisters.insert(outputToRegister[startNode]);
        allIntermediateRegisters.insert(outputToRegister[startNode]);
        return;
    }
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    int i;
    outputToInputItr = outputToInput.find(startNode);
    if(outputToInputItr != outputToInput.end())
    {
        for(i=0;i<outputToInputItr->second.size();i++)
        {
            countIntermediateRegisters(outputToInputItr->second[i] , visitedNodes , intermediateRegisters , allIntermediateRegisters);
        }
    }

}


/*
    initiate the count the number of intermediate registers dependent
*/
void initiateCountIntermediateRegisters()
{
    unordered_map<string,bool> visitedNodes;
    unordered_set<string>::iterator nodesItr;
    unordered_set<string> intermediateRegisters;
    unordered_set<string> allIntermediateRegisters;
    //vector<string> nextStates{"_next_state_reg_1_" , "_next_state_reg_2_" , "_next_state_reg_3_" , "_next_state_reg_4_" , "_next_state_reg_5_" , "_next_state_reg_6_" , "_next_state_reg_7_" , "_next_state_reg_8_" , "_next_state_reg_9_"};
    //vector<string> nextStates{"next_state_1_" , "next_state_2_" , "next_state_3_" , "next_state_4_" , "next_state_5_" , "next_state_6_" , "next_state_7_" , "next_state_8_" , "next_state_9_"};
    vector<string> nextStates{"______9_________________0____________0___9__________0_","__________________9_____________________________1006044","__________________9_____________________________1015435","__________________9_____________________________1004806","__________________9________________0___________990868","__________________9_____________________________1016191","__________________9_____________________________981413","__________________9___________________________0_1017779","__________________9________________0____________1005161","__________________9_____________________________1002215","__________________9_____________________________986023","__________________9____________________________991840","__________________9________________0_________9_","__________________9________________0___________991981","__________________9________________0____________1013928","__________________9________________0____________1002873","__________________9________________0__________0_1016905","__________________9____________________________992842","__________________9___________________________0_1010964","__________________9__________________________0_","__________________9________________0____________1004146","__________________9________________0____________1011442","__________________9________________0__________0_1010051","__________________9____________________________996297","__________________9___________________________9_","__________________9________________0____________1012341","__________________9________________0___________994654","__________________9____________________________995409","__________________9________________0___________995762","__________________9____________________________","__________________9____________________________998244","__________________9________________0____________1006386","__________________9________________0___________997897","__________________9________________0__________9_1008989","__________________9_____________________________1019302","__________________9____________________________994126","__________________9________________0____________1001434","__________________________________0__________0_774114","___________________0______________0____________915563","__________________9_____________________________1065178","_______________________9_0___________0_________________1071890","__________________9__________________________9_","__________________9____________________________997344","__________________9________________0____________986993","__________________9________________0____________985297","__________________9___________________________0_","__________________9________________0__________0_"};
    vector<string>::iterator nextStatesItr;
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    int i;

    for(nextStatesItr = nextStates.begin() ; nextStatesItr != nextStates.end() ; nextStatesItr++)
    {
        intermediateRegisters.clear();
        for(nodesItr=nodes.begin();nodesItr!=nodes.end();nodesItr++)
        {
            visitedNodes[*nodesItr] = false;
        }
        //outputToInputItr = outputToInput.find(registerToInput[*nextStatesItr]);
        outputToInputItr = outputToInput.find(*nextStatesItr);
        cout<<*nextStatesItr<<" : ";
        if(outputToInputItr != outputToInput.end())
        {
            for(i=0;i<outputToInputItr->second.size();i++)
            {
                countIntermediateRegisters(outputToInputItr->second[i] , visitedNodes , intermediateRegisters , allIntermediateRegisters);
            }
        }
        cout<<"Count : "<<intermediateRegisters.size()<<"\n";
        unordered_set<string>::iterator intermediateRegistersItr;
        for(intermediateRegistersItr=intermediateRegisters.begin();intermediateRegistersItr!=intermediateRegisters.end();intermediateRegistersItr++)
        {
            cout<<*intermediateRegistersItr<<"\n";
        }
        cout<<"\n\n";
    }
    cout<<"Total Count : "<<allIntermediateRegisters.size()<<"\n";
    unordered_set<string>::iterator allIntermediateRegistersItr;
    for(allIntermediateRegistersItr=allIntermediateRegisters.begin();allIntermediateRegistersItr!=allIntermediateRegisters.end();allIntermediateRegistersItr++)
    {
        cout<<*allIntermediateRegistersItr<<"\n";
    }

}


void traceMuxElements(string startNode , unordered_map<string,bool> &visitedNode , unordered_set<string> &dependentRegisters , unordered_set<string> &graphPaths)
{
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    int i;
    if(visitedNode[startNode])
        return;
    visitedNode[startNode] = true;
    if(operatorOperand[startNode].substr(0,2) == "df")
    {
        // cout<<outputToRegister[startNode]<<"\n";
        // cout<<startNode<<" -> "<<outputToRegister[startNode]<<"\n";
        graphPaths.insert(outputToRegister[startNode] + "[ shape = \"rectangle\" ; style = \"filled\" ; color = \"grey\"]");
        graphPaths.insert(outputToRegister[startNode] + " -> " + startNode);
        dependentRegisters.insert(outputToRegister[startNode]);
        return;
    }
    outputToInputItr = outputToInput.find(startNode);
    if(outputToInputItr != outputToInput.end())
    {
        for(i=0;i<outputToInputItr->second.size();i++)
        {
            // cout<<outputToRegister[startNode]<<" -> "<<startNode<<"\n";
            // cout<<outputToInputItr->second[i]<<" -> "<<outputToRegister[startNode]<<"\n";
            graphPaths.insert(outputToRegister[startNode] + "[ shape = \"rectangle\"]");
            graphPaths.insert(outputToRegister[startNode] + " -> " + startNode);
            graphPaths.insert(outputToInputItr->second[i] + " -> " + outputToRegister[startNode]);
            traceMuxElements(outputToInputItr->second[i] , visitedNode , dependentRegisters , graphPaths);
        }
    }
}

void initiateTraceMuxElements(string startNode)
{
    unordered_map<string,bool> visitedNode;
    unordered_set<string> dependentRegisters;
    unordered_set<string> graphPaths;
    unordered_set<string>::iterator nodesItr;
    unordered_map<string,vector<string> >::iterator outputToInputItr;
    unordered_set<string>::iterator dependentRegistersItr;
    unordered_set<string>::iterator graphPathsItr;
    int i;
    for(nodesItr=nodes.begin();nodesItr!=nodes.end();nodesItr++)
    {
        visitedNode[*nodesItr] = false;
    }
    outputToInputItr = outputToInput.find(startNode);
    if(outputToInputItr != outputToInput.end())
    {
        for(i=0;i<outputToInputItr->second.size();i++)
        {
            // cout<<outputToRegister[startNode]<<" -> "<<startNode<<"\n";
            // cout<<outputToInputItr->second[i]<<" -> "<<outputToRegister[startNode]<<"\n";
            if(operatorOperand[startNode].substr(0,2) == "df")
            {
                // cout<<outputToRegister[startNode]<<"\n";
                // cout<<startNode<<" -> "<<outputToRegister[startNode]<<"\n";
                graphPaths.insert(outputToRegister[startNode] + "[ shape = \"rectangle\" ; style = \"filled\" ; color = \"grey\"]");
                graphPaths.insert(outputToRegister[startNode] + " -> " + startNode);
                dependentRegisters.insert(outputToRegister[startNode]);
                continue;
            }
            graphPaths.insert(outputToRegister[startNode] + "[ shape = \"rectangle\"]");
            graphPaths.insert(outputToRegister[startNode] + " -> " + startNode);
            graphPaths.insert(outputToInputItr->second[i] + " -> " + outputToRegister[startNode]);
            traceMuxElements(outputToInputItr->second[i] , visitedNode , dependentRegisters , graphPaths);
        }
    }
    cout<<"Count : "<<dependentRegisters.size()<<"\n";
    for(dependentRegistersItr = dependentRegisters.begin() ; dependentRegistersItr != dependentRegisters.end() ; dependentRegistersItr++)
    {
        cout<<*dependentRegistersItr<<"\n";
    }
    // for(graphPathsItr = graphPaths.begin() ; graphPathsItr != graphPaths.end() ; graphPathsItr++)
    // {
    //     cout<<*graphPathsItr<<"\n";
    // }
}

void print(){
    cout<<" -----------------outputToInput----------------";
    cout<<endl;
    for(auto it : outputToInput){
        cout<<it.first<<" : ";
        for(auto jt : it.second){
            cout<<jt<<"  ";
        }
        cout<<endl;
    }

    cout<<" -----------------inputToOutput----------------";
    cout<<endl;
    for(auto it : inputToOutput){
        cout<<it.first<<" : ";
        for(auto jt : it.second){
            cout<<jt<<"  ";
        }
        cout<<endl;
    }

    cout<<" -----------------regOutputType----------------";
    cout<<endl;
    for(auto it : regOutputType){
        cout<<it.first<<" : "<<it.second;
        cout<<endl;
    }

    cout<<" -----------------operatorOperand----------------";
    cout<<endl;
    for(auto it : operatorOperand){
        cout<<it.first<<" : ";
        for(auto jt : it.second){
            cout<<jt<<"  ";
        }
        cout<<endl;
    }

    cout<<" -----------------variableComputed----------------";
    cout<<endl;
    for(auto it : variableComputed){
        cout<<it.first<<" : "<<it.second;
        
    }
    cout<<endl;

    cout<<" -----------------pathDetails----------------";
    cout<<endl;
    for(auto it : pathDetails){
        cout<<it<<" ";
        
    }
    cout<<endl;

    cout<<" -----------------nodes----------------";
    cout<<endl;
    for(auto it : nodes){
        cout<<it<<" ";
        
    }
    cout<<endl;

    cout<<" -----------------registerToInput----------------";
    cout<<endl;
    for(auto it : registerToInput){
        cout<<it.first<<" : "<<it.second;
        cout<<endl;
        
    }
    cout<<endl;
    cout<<" -----------------outputToRegister----------------";
    cout<<endl;
    for(auto it : outputToRegister){
        cout<<it.first<<" : "<<it.second;
        cout<<endl;
        
    }
    cout<<" -----------------registerToOutput----------------";
    cout<<endl;
    for(auto it : registerToOutput){
        cout<<it.first<<" : ";
        for(auto jt : it.second){
            cout<<jt<<"  ";
        }
        cout<<endl;
    }

    cout<<" -----------------nextStates----------------";
    cout<<endl;
    for(auto it : nextStates){
        cout<<it<<" ";
    }
    cout<<endl;

    cout<<" -----------------currentStates----------------";
    cout<<endl;
    for(auto it : currentStates){
        cout<<it<<" ";
    }
    cout<<endl;

    cout<<" -----------------registerList----------------";
    cout<<endl;
    for(auto it : registerList){
        cout<<it<<" ";
    }
    cout<<endl;
}



int main(int agrc , char** argv)
{
    filename = argv[1];
    constructGraph();
    // print();
    vector<string> registers{"__________________36279" , "__________________36259" , "__________________36250","__________________36155","__________","________________0_","__________________","__________________36230"};
    vector<string> registersOriginal{"_curr_state_reg_1_","_curr_state_reg_2_","_curr_state_reg_3_","_curr_state_reg_4_","_curr_state_reg_5_","_curr_state_reg_6_","_curr_state_reg_7_","_curr_state_reg_0_","_next_state_reg_1_","_next_state_reg_2_","_next_state_reg_3_","_next_state_reg_4_","_next_state_reg_5_","_next_state_reg_6_","_next_state_reg_7_","_next_state_reg_0_","_OP_reg_0_","_OP_reg_1_"};

    // for getting the dependency of an element
    vector<string>::iterator registersItr;
    for(registersItr = registers.begin() ; registersItr != registers.end() ; registersItr++)
    {
        cout<<*registersItr<<":";
        initiateTraceMuxElements(registerToInput[*registersItr]);
        cout<<"\n\n";

    }
    initiateTraceMuxElements(argv[2]);

    initiateDFS("___09___2017");


    cout<<"\n\n";
    initiateTraceMuxElements("n581");
    cout<<"\n\n";
    initiateTraceMuxElements("n582");
    findPaths("__9____1926","__________________36155");
    initiatePrintNextStateToCurrentState(argv[2]);
    verilogToBench();
    
    initiateFindPath();
   
    cout<<"digraph G {";

    getPath(argv[2]);

    getPathInputToOutput("next_state_7_");

    initiateCheckCycle();
    unordered_set<string>::iterator cycleRegistersListItr;
    for(cycleRegistersListItr=cycleRegistersList.begin();cycleRegistersListItr!=cycleRegistersList.end();cycleRegistersListItr++)
    {
        cout<<*cycleRegistersListItr<<"\n";
    }

    initiateMakePath();
    printGraph(stateGraph);

    printBench(reverseStateGraph);

    printGraphNode(argv[2]);

    unordered_map<string,vector<string> >::iterator invOutputToRegistersItr;
    int totalPairsCount = 0;
    for(invOutputToRegistersItr=invOutputToRegisters.begin();invOutputToRegistersItr!=invOutputToRegisters.end();invOutputToRegistersItr++)
    {
        cout<<invOutputToRegistersItr->first<<" "<<invOutputToRegistersItr->second.size()<<"\n";
        totalPairsCount+=invOutputToRegistersItr->second.size();
        for(int i=0;i<invOutputToRegistersItr->second.size();i++)
        {
            cout<<invOutputToRegistersItr->second[i]<<"\n";
        }
        cout<<"\n\n";
    }

    unordered_map<string,vector< pair<string,string> > >::iterator registerPairItr;
    for(registerPairItr=registerPair.begin();registerPairItr!=registerPair.end();registerPairItr++)
    {
        int pairCount = 0;
        // cout<<registerPairItr->first<<" "<<registerPairItr->second.size();
        // totalPairsCount+=registerPairItr->second.size();
        for(int i=0;i<registerPairItr->second.size();i++)
        {
            if(registerOccuranceCount[registerPairItr->second[i].second] == 1 && registerOccuranceCount[registerPairItr->second[i].first] == 1)
            {
                //cout<<registerPairItr->second[i].first<<" -> "<<registerPairItr->second[i].second<<"\n";
                nextStates.push_back(registerPairItr->second[i].first);
                currentStates.push_back(registerPairItr->second[i].second);           
                pairCount++;
            }
        }
        //cout<<registerPairItr->first<<" : "<<pairCount;
        totalPairsCount+=pairCount;
        //cout<<"\n\n";
    }

    cout<<"Total Pairs : "<<totalPairsCount;
    
    
    initiateCountIntermediateRegisters();

    initiateGetCurrentStateToNextStateCount();

    unordered_map<string,int>::iterator registerOccuranceCountItr;
    for(registerOccuranceCountItr=registerOccuranceCount.begin();registerOccuranceCountItr!=registerOccuranceCount.end();registerOccuranceCountItr++)
    {
        if(registerOccuranceCountItr->second > 1)
            cout<<registerOccuranceCountItr->first<<"\n";
    }
    // unordered_set<string>::iterator cycleRegistersListItr;
    for(cycleRegistersListItr=cycleRegistersList.begin();cycleRegistersListItr!=cycleRegistersList.end();cycleRegistersListItr++)
    {
        cout<<*cycleRegistersListItr<<"\n";
    }
    
    bool flag = 0;
    for(auto regItr=operatorOperand.begin();regItr!=operatorOperand.end();regItr++)
    {
        if(regItr->second.substr(0,2) == "df")
        {
            auto outToIntItr = inputToOutput.find(regItr->first);
            if(outToIntItr == inputToOutput.end())
                continue;
            //cout<<regItr->first<<" : "<<outToIntItr->second.size();
            if(outToIntItr->second.size() == 1)
            {
                flag = 1;
                cout<<regItr->first<<" : "<<operatorName[regItr->first];
            }
        }
        if(flag)
        {
            flag = 0;
            cout<<"\n";
        }
    }
    cout<<"}";
    return 0;
}

