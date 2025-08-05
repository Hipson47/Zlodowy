import React from 'react';
import { render } from '@testing-library/react';
import HomePage from '../app/page';

// Mock the ChatInterface and Header components
jest.mock('@/components/ChatInterface', () => () => <div>Chat Interface Mock</div>);
jest.mock('@/components/Header', () => () => <div>Header Mock</div>);

describe('HomePage', () => {
  it('renders the welcome page correctly', () => {
    const { asFragment } = render(<HomePage />);
    // Initial render should show the welcome message and "Start Chatting" button
    expect(asFragment()).toMatchSnapshot();
  });
});
