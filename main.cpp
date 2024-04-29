

int main() {
  SDL_Window* window = SDL_CreateWindow("Esc CZ", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1000, 1000, 0);
  SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
  int running = 1;
  while (running) {
    if (SDL_QuitRequested()) {
      running = 0;
      break;
    }
  }
  return 0;
}
