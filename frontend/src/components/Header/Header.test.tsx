import React from 'react';
import { render, screen } from '@testing-library/react';
import Header from './index';

describe('Header', () => {
  it('renders the logo text', () => {
    render(<Header />);
    expect(screen.getByText('Zlodowy')).toBeInTheDocument();
  });

  it('renders navigation links', () => {
    render(<Header />);
    expect(screen.getByText('Features')).toBeInTheDocument();
    expect(screen.getByText('About')).toBeInTheDocument();
    expect(screen.getByText('GitHub')).toBeInTheDocument();
  });

  it('applies custom className when provided', () => {
    const customClass = 'custom-header-class';
    render(<Header className={customClass} />);
    const header = screen.getByRole('banner');
    expect(header).toHaveClass(customClass);
  });
}); 