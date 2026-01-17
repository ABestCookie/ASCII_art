#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <chrono>
#include <thread>
#include <cstdlib>

#ifdef _WIN32
    #define CLEAR_COMMAND "cls"
#else
    #define CLEAR_COMMAND "clear"
#endif

using namespace std;



vector<string> loadFramesFromFile(const string& path, const string& delimiter = "===FRAME===") {
    ifstream file(path);
    if (!file.is_open()) {
        cerr << "Error: Cannot open file " << path << endl;
        return {};
    }

    string content((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
    file.close();

    vector<string> frames;
    size_t start = 0;
    size_t end = content.find(delimiter);

    while (end != string::npos) {
        string frame = content.substr(start, end - start);
        
        // 移除前後空白
        size_t first = frame.find_first_not_of(" \t\n\r");
        size_t last = frame.find_last_not_of(" \t\n\r");
        if (first != string::npos) {
            frame = frame.substr(first, (last - first + 1));
            if (!frame.empty()) {
                frames.push_back(frame);
            }
        }
        
        start = end + delimiter.length();
        end = content.find(delimiter, start);
    }

    // 處理最後一個幀
    string lastFrame = content.substr(start);
    size_t first = lastFrame.find_first_not_of(" \t\n\r");
    size_t last = lastFrame.find_last_not_of(" \t\n\r");
    if (first != string::npos) {
        lastFrame = lastFrame.substr(first, (last - first + 1));
        if (!lastFrame.empty()) {
            frames.push_back(lastFrame);
        }
    }

    return frames;
}

void playAnimation(const vector<string>& frames, int delayMs) {
    for (const auto& frame : frames) {
        system(CLEAR_COMMAND);
        cout << frame + "\n";
        this_thread::sleep_for(chrono::milliseconds(delayMs));
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string asciiFile = "ascii_animation.txt";
    int delayMs = 0;  // 延遲時間（毫秒）

    auto frames = loadFramesFromFile(asciiFile);
    
    if (frames.empty()) {
        cerr << "Error: No frames loaded" << endl;
        return 1;
    }

    cout << "🎬 共載入 " << frames.size() << " 幀，開始播放.../n";
    this_thread::sleep_for(chrono::seconds(1));

    playAnimation(frames, delayMs);

    return 0;
}
