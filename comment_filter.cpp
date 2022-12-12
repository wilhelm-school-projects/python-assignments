#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

const string ALPHABET {"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"};

string construct_output_name(string const& filename);

bool is_comment_row(string const& buffer);


int main(int argc, char** argv)
{
    if (argc != 2)
    {
        cout << "Usage: ./a.out pythonfile" << endl;
        return 1;
    }
    
    string filename {argv[1]};
    ifstream in_file {filename};

    string output_filename { construct_output_name(filename) };
    ofstream result_file { output_filename, std::ios_base::out};
    
    string buffer {};
    string result {};
    
    // Write the first two lines (shebang and encoding)
    getline(in_file, buffer);
    result_file << buffer << "\n";
    getline(in_file, buffer);
    result_file << buffer << "\n";

    result_file << '\n' <<"# Sorry for all the newlines above. My script \n# for removing only-comment-rows isn't very sophisticated." << endl;


    bool prev_was_comment_row {false};
    while ( getline(in_file, buffer) )
    {
        if ( is_comment_row(buffer) )
        {
            prev_was_comment_row = true;
            continue;
        }

        if ( prev_was_comment_row && buffer.empty() )
        {
            continue;
        }

        result += buffer + '\n';
        cout << buffer << endl;
        cout << "----------------------------------------------" << endl;
        prev_was_comment_row = false;
    }
    result_file << result;

    result_file.close();
    in_file.close();

    return 0;
}

string construct_output_name(string const& filename)
{
    auto dot { find(begin(filename), end(filename), '/') };
    string result { "result_"};
    string tmp { dot + 1, end(filename) };
    result += tmp;
    return result;
}


bool is_comment_row(string const& buffer)
{
    if ( buffer.empty() )
    {
        return false;
    }

    auto start { begin(buffer) };
    auto last { end(buffer) };
    auto comment_sign { find(start, last, '#') };

    // Didn't find any '#', therefore is not comment row
    if (comment_sign == last)
    {
        return false;
    }

    // Did find a alphabetic word before the comment sign '#' there is not comment_row 
    auto result { find_first_of(start, comment_sign, begin(ALPHABET), end(ALPHABET) ) };
    if ( result != comment_sign )
    {
        return false;
    }

    // This is for sure a comment row
    return true;

}